# T02 — Code Scaffold (`judge-bias-eval`)

*Repo*: `github.com/rohithreddybc/judge-bias-eval` (to be created)
*License*: MIT
*Python*: 3.10+

---

## Repo layout

```
judge-bias-eval/
├── README.md
├── LICENSE
├── pyproject.toml          # pip-installable
├── requirements.txt
├── Dockerfile              # for reviewer reproducibility
├── judge_bias_eval/
│   ├── __init__.py
│   ├── clients/            # API client wrappers (one per provider)
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── openai_client.py
│   │   ├── anthropic_client.py
│   │   ├── together_client.py
│   │   ├── google_client.py
│   │   └── retry.py        # exponential backoff + budget cap
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── pairwise_summary.py
│   │   ├── pairwise_qa.py
│   │   └── pointwise_code.py
│   ├── judge.py            # core: invoke a judge with (item, condition)
│   ├── conditions.py       # C1..C4 position-condition definitions
│   ├── pbi.py              # Position Bias Index computation
│   ├── stability.py        # Kendall-τ, rank-order analyses
│   ├── stats.py            # bootstrap CIs, BH correction
│   ├── budget.py           # per-task and per-model spend caps
│   └── cli.py              # `judge-bias-eval run`, `judge-bias-eval analyze`
├── data/
│   ├── prompts/            # prompt templates per task
│   ├── items/              # input items per task (200 each)
│   └── runs/               # outputs (gitignored except small samples)
├── notebooks/
│   ├── 01_pilot.ipynb      # week-3 pilot inspection
│   ├── 02_main_analysis.ipynb
│   └── 03_figures.ipynb    # paper figures
├── tests/
│   ├── test_pbi.py
│   ├── test_stability.py
│   ├── test_judge.py       # mocked client; no network
│   └── test_conditions.py
└── results/
    ├── pbi_per_model_task.csv
    ├── kendall_tau.csv
    └── figures/
```

---

## Core APIs

### `JudgeClient` (clients/base.py)

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class JudgeResponse:
    raw: str                   # full text response
    parsed: dict               # parsed structured output
    cost_usd: float            # incurred cost
    latency_s: float

class JudgeClient(ABC):
    name: str                  # "gpt-4o-2024-08-06" etc.
    family: str                # "openai" / "anthropic" / "meta" / "mistral" / "google"

    @abstractmethod
    def judge(self, prompt: str, *, max_tokens: int = 200,
              temperature: float = 0.0, seed: int = 42) -> JudgeResponse: ...
```

### `Condition` (conditions.py)

```python
from enum import Enum
class Condition(str, Enum):
    A_FIRST  = "C1_A_first"
    B_FIRST  = "C2_B_first"
    RANDOM   = "C3_random"     # 5 trials, majority vote
    BLINDED  = "C4_blinded"    # both labelled "Response 1", "Response 2", no other cue
```

### `Item` and `JudgeCall` (judge.py)

```python
@dataclass
class Item:
    item_id: str
    task: str                  # "T-Sum" / "T-QA" / "T-Code"
    candidate_a: str
    candidate_b: str
    quality_label: str | None  # "TIE" / "A_BETTER" / "B_BETTER"
    metadata: dict

@dataclass
class JudgeCall:
    call_id: str
    item: Item
    judge: str
    condition: Condition
    prompt: str
    response: JudgeResponse
    decision: str              # "A" / "B" / "TIE" / "PARSE_ERROR"
    timestamp: str             # ISO 8601 UTC
```

### `pbi.py`

```python
def position_bias_index(calls: list[JudgeCall], judge: str, task: str) -> dict:
    """
    Returns: {
      "judge": str,
      "task": str,
      "n_a_first": int,
      "n_b_first": int,
      "p_picks_position_1_when_a_first": float,
      "p_picks_position_1_when_b_first": float,
      "pbi": float,                        # |p1 - p2| (raw)
      "pbi_normalised": float,             # 2 * |0.5 * (p1 + p2) - 0.5|
      "pbi_ci_low_95": float,              # bootstrap
      "pbi_ci_high_95": float,
      "n_calls_used": int,
    }
    """
```

### `stability.py`

```python
def kendall_tau_under_swap(items: list[Item], judge: str,
                           leaderboard_size: int) -> dict:
    """
    For each leaderboard of size N (sampled from items), compute
    rankings under C1 (all A_first) and C2 (all B_first), then
    Kendall's τ between the two.
    Returns: { "n": int, "tau_mean": float, "tau_ci": (float, float) }
    """
```

### Budget cap (budget.py)

```python
class BudgetCap:
    def __init__(self, total_usd: float = 1500.0,
                 per_model_usd: dict[str, float] | None = None):
        self.total_usd = total_usd
        self.spent_usd = 0.0
        self.per_model_spent = {}
        self.per_model_cap = per_model_usd or {}

    def can_spend(self, model: str, estimated_usd: float) -> bool:
        if self.spent_usd + estimated_usd > self.total_usd: return False
        cap = self.per_model_cap.get(model, float("inf"))
        if self.per_model_spent.get(model, 0.0) + estimated_usd > cap: return False
        return True

    def record(self, model: str, actual_usd: float) -> None:
        self.spent_usd += actual_usd
        self.per_model_spent[model] = self.per_model_spent.get(model, 0.0) + actual_usd
```

---

## CLI

```bash
# Run a single (model, task, condition) cohort
judge-bias-eval run --model gpt-4o --task T-Sum --condition C1 --n 200

# Run the full grid
judge-bias-eval run-all --config configs/main.yaml

# Analyse: produce PBI tables and figures
judge-bias-eval analyze --runs data/runs/ --out results/

# Sanity check: replay one call from a run log
judge-bias-eval replay --run-id <id> --call-id <id>
```

---

## Configuration (`configs/main.yaml`)

```yaml
budget:
  total_usd: 1500
  per_model_usd:
    gpt-4o-2024-08-06: 400
    claude-3-5-sonnet-20241022: 400
    llama-3.3-70b-instruct: 200
    mistral-large-2: 300
    gemini-2.0-flash: 100

models:
  - id: gpt-4o-2024-08-06
    family: openai
    client: openai
  - id: claude-3-5-sonnet-20241022
    family: anthropic
    client: anthropic
  - id: llama-3.3-70b-instruct
    family: meta
    client: together
  - id: mistral-large-2
    family: mistral
    client: together
  - id: gemini-2.0-flash
    family: google
    client: google

tasks:
  - id: T-Sum
    n_items: 200
    source: cnn_dailymail_validation
    pair_construction: human_labelled_ties
  - id: T-QA
    n_items: 200
    source: truthfulqa
    pair_construction: paraphrase
  - id: T-Code
    n_items: 200
    source: humaneval_perturbed
    pair_construction: pointwise

conditions:
  - C1_A_first
  - C2_B_first
  - C3_random
  - C4_blinded

stats:
  bootstrap_n: 1000
  ci: 0.95
  multiple_comparisons: bh
  q: 0.05
  random_seed: 42
```

---

## Logging discipline

Every judge call writes one JSON line to `data/runs/<run_id>.jsonl`:

```json
{
  "call_id": "uuid4",
  "timestamp": "2026-06-01T12:34:56Z",
  "model": "gpt-4o-2024-08-06",
  "task": "T-Sum",
  "condition": "C1_A_first",
  "item_id": "cnn_001",
  "prompt_sha256": "abc123...",
  "prompt_excerpt": "...first 200 chars...",
  "response_raw": "...full response...",
  "decision": "A",
  "cost_usd": 0.0042,
  "latency_s": 1.23,
  "client_version": "openai-python==1.50.0"
}
```

This means: **every figure in the paper traces back to a specific JSONL record**.
A reviewer can grep for any decision and audit the full prompt + response.

---

## What we will NOT do

- No fine-tuning. No training. Pure inference + analysis.
- No new dataset. We use existing benchmarks.
- No new judge architecture. We characterise existing judges.
- No human evaluation step (cost + IRB risk). All "ground truth" comes from
  existing labelled datasets.

These exclusions keep scope tight enough for a 4–6 month solo project.

---

## Build order (week-by-week)

**Week 1**: `clients/` (4 of 5 providers), `judge.py`, `conditions.py`, mock-tested
**Week 2**: `tasks/` (data loaders for 3 tasks), prompt templates
**Week 3**: Pilot — one task × two judges, manually inspect 50 outputs
**Week 4–6**: Full grid run via `cli.py run-all`
**Week 7**: `pbi.py`, `stats.py`, initial tables
**Week 8**: `stability.py`, `notebooks/02_main_analysis.ipynb`
**Week 9–10**: `notebooks/03_figures.ipynb`, paper draft
**Week 11+**: Revisions, README polish, v1.0 release tag
