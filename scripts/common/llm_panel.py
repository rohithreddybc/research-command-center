"""
LLM reviewer panel.

Default provider: Claude Code CLI (`claude -p`) — runs on the user's Max plan,
NOT the Anthropic API. No charges; no API key required.

OpenAI is opt-in and strictly used as a tiebreaker. Budget is bounded.

Reviewers see ONLY the assembled evidence packet, never their own memory.

Caching: every (role, packet-hash) pair is cached on disk so repeated runs
are free.
"""
from __future__ import annotations
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
LLM_CACHE = REPO_ROOT / "data" / "cache" / "llm_cache"
LLM_CACHE.mkdir(parents=True, exist_ok=True)
OPENAI_BUDGET_FILE = REPO_ROOT / "data" / "cache" / "openai_budget.json"
DEFAULT_OPENAI_BUDGET = 8  # max tiebreaker calls per pipeline run, total
INBOX_DIR = REPO_ROOT / "data" / "reviews" / "_inbox"
INBOX_DIR.mkdir(parents=True, exist_ok=True)

# Per-process error accumulator. 06_llm_review_topics flushes this to
# reports/llm_review_errors.md when the run finishes.
ERRORS: list[dict[str, Any]] = []


def record_error(provider: str, role: str, topic_id: str, message: str) -> None:
    ERRORS.append({
        "provider": provider, "role": role, "topic_id": topic_id, "message": message[:500],
    })


def _load_dotenv() -> None:
    repo = REPO_ROOT
    env_file = repo / ".env"
    if not env_file.exists():
        return
    try:
        for raw in env_file.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v
    except Exception:
        pass


_load_dotenv()


# ---------- providers ----------

def _find_claude_cli() -> str | None:
    env_path = os.environ.get("CLAUDE_CLI_PATH")
    if env_path and Path(env_path).exists():
        return env_path
    on_path = shutil.which("claude") or shutil.which("claude.exe")
    if on_path:
        return on_path
    candidates = [
        Path(os.environ.get("APPDATA", "")) / "Claude" / "claude-code",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "claude-code",
    ]
    for c in candidates:
        if c.exists():
            versions = sorted([d for d in c.iterdir() if d.is_dir()], reverse=True)
            for v in versions:
                exe = v / "claude.exe"
                if exe.exists():
                    return str(exe)
                exe = v / "claude"
                if exe.exists():
                    return str(exe)
    return None


CLAUDE_CLI = _find_claude_cli()


try:
    from openai import OpenAI  # type: ignore
    HAS_OPENAI = True
except Exception:
    HAS_OPENAI = False


def have_claude_cli() -> bool:
    return bool(CLAUDE_CLI)


def have_openai_key() -> bool:
    return HAS_OPENAI and bool(os.environ.get("OPENAI_API_KEY"))


# ---------- reviewer roles ----------
# DEFAULT panel: 8 academic-neutral reviewers. The two personal-goal reviewers
# (niw_eb1a, career_faang) are EXCLUDED by default. To include them, the
# orchestrator must call get_reviewer_roles(include_personal_goals=True),
# which is gated behind the --include-personal-goals CLI flag.

NEUTRAL_REVIEWER_ROLES: list[dict[str, str]] = [
    {"role": "citation_potential",
     "focus": "Will this paper attract citations? Audience size, gap clarity, reusability. Do not favor any field."},
    {"role": "novelty_saturation",
     "focus": "Is the gap real? Is the area saturated? Is differentiation specific? Do not infer novelty from absence of search results — absence may be query bias."},
    {"role": "venue_publication",
     "focus": "Is there a credible venue path? Venue must be peer-reviewed and indexed (DBLP, PubMed, Scopus). Do not favor open-access or no-APC venues over high-prestige closed venues."},
    {"role": "artifact_reproducibility",
     "focus": "Will the artifact be reusable? Reproducibility risk? Do not require an artifact contribution — pure-paper contributions can be equally valuable."},
    {"role": "methodological_rigor",
     "focus": "Methodological soundness, statistical design, evaluation protocol. Reject methodologically weak topics regardless of field."},
    {"role": "feasibility_resources",
     "focus": "Resource feasibility (data access, compute, time, IRB). Realistic scope for a single author within 12 months."},
    {"role": "existing_work_overlap",
     "focus": "Are there peer-reviewed papers, GitHub repos, or HuggingFace artifacts that already deliver this contribution? Be specific."},
    {"role": "brutal_skeptic",
     "focus": "What is the strongest reason this topic will fail or be rejected? Do not favor topics in any specific field, methodology, or artifact type."},
]

# Optional, included only with --include-personal-goals
PERSONAL_GOAL_REVIEWERS: list[dict[str, str]] = [
    {"role": "niw_eb1a",
     "focus": "Does this build NIW prong-2/3 evidence and EB-1A scholarly-articles + original-contributions evidence?"},
    {"role": "career_faang",
     "focus": "Does this build evidence for high-paying ML/data-science roles?"},
]


def get_reviewer_roles(include_personal_goals: bool = False) -> list[dict[str, str]]:
    """Return the active reviewer-role list.

    Default: 8 academic-neutral reviewers (NEUTRAL_REVIEWER_ROLES).
    With include_personal_goals=True: appends the 2 personal-goal reviewers.

    The 8 neutral default and the 10-reviewer extended set are both valid;
    callers that don't pass the flag will not include personal-goal reviewers.
    """
    roles = list(NEUTRAL_REVIEWER_ROLES)
    if include_personal_goals:
        roles.extend(PERSONAL_GOAL_REVIEWERS)
    return roles


# Backward-compat alias. NEW CODE SHOULD USE get_reviewer_roles().
# This alias preserves the *neutral* default panel — it does NOT include
# personal-goal reviewers. Callers that want the legacy 8-reviewer panel
# (with niw_eb1a and career_faang) must explicitly call
# get_reviewer_roles(include_personal_goals=True).
REVIEWER_ROLES = list(NEUTRAL_REVIEWER_ROLES)


SYSTEM_PROMPT = """You are a skeptical research reviewer.

Rules:
- Use ONLY the evidence packet provided. Do NOT use any prior knowledge of specific papers, citation counts, venue APCs, or deadlines from your memory.
- Do not favor healthcare, LLM evaluation, JudgeSense, NIW, EB1A, FAANG, or the user's background unless the retrieved evidence itself supports relevance. Judge only from the evidence packet.
- Do not favor any specific contribution type (no preference for benchmarks over theory papers, datasets over surveys).
- Do not favor open-access or no-APC venues over peer-reviewed closed-access venues.
- If the evidence packet does not support a claim, say so in `evidence_missing`.
- Output STRICT JSON matching the schema. No prose outside JSON.
- decision must be one of: GO, NARROW, DROP, NEEDS_MORE_EVIDENCE.
- confidence must be one of: LOW, MEDIUM, HIGH.
- score is an integer 1..5 (5 best).

Schema:
{
  "reviewer_role": str,
  "score": int,
  "decision": "GO"|"NARROW"|"DROP"|"NEEDS_MORE_EVIDENCE",
  "confidence": "LOW"|"MEDIUM"|"HIGH",
  "evidence_used": [str],
  "evidence_missing": [str],
  "biggest_risk": str,
  "recommendation": str
}
"""


# ---------- packet & caching ----------

def _packet_hash(role: str, topic: dict[str, Any], evidence: dict[str, Any]) -> str:
    h = hashlib.sha256()
    h.update(role.encode("utf-8"))
    h.update(json.dumps(topic, sort_keys=True, default=str).encode("utf-8"))
    h.update(json.dumps(evidence, sort_keys=True, default=str).encode("utf-8"))
    return h.hexdigest()[:24]


def _cache_path(role: str, topic_id: str, packet_hash: str) -> Path:
    return LLM_CACHE / f"{topic_id}_{role}_{packet_hash}.json"


def _user_prompt(role: dict[str, str], topic: dict[str, Any], evidence: dict[str, Any]) -> str:
    return (
        f"REVIEWER ROLE: {role['role']}\n"
        f"FOCUS: {role['focus']}\n\n"
        f"TOPIC:\n{json.dumps(topic, ensure_ascii=False, indent=2)}\n\n"
        f"EVIDENCE PACKET (only source of truth):\n{json.dumps(evidence, ensure_ascii=False, indent=2)[:60000]}\n\n"
        "Return JSON only."
    )


def _extract_json(text: str) -> dict[str, Any] | None:
    if not text:
        return None
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        cleaned = re.sub(r",(\s*[}\]])", r"\1", m.group(0))
        try:
            return json.loads(cleaned)
        except Exception:
            return None


def _normalize(obj: dict[str, Any], role: str) -> dict[str, Any]:
    valid_dec = {"GO", "NARROW", "DROP", "NEEDS_MORE_EVIDENCE"}
    valid_conf = {"LOW", "MEDIUM", "HIGH"}
    out = {
        "reviewer_role": role,
        "score": 0,
        "decision": "NEEDS_MORE_EVIDENCE",
        "confidence": "LOW",
        "evidence_used": [],
        "evidence_missing": [],
        "biggest_risk": "",
        "recommendation": "",
    }
    if not isinstance(obj, dict):
        return out
    s = obj.get("score", 0)
    try:
        out["score"] = max(1, min(5, int(s)))
    except Exception:
        out["score"] = 0
    d = str(obj.get("decision", "")).upper().replace("-", "_").replace(" ", "_")
    if d in valid_dec:
        out["decision"] = d
    c = str(obj.get("confidence", "")).upper()
    if c in valid_conf:
        out["confidence"] = c
    for k in ("evidence_used", "evidence_missing"):
        v = obj.get(k, [])
        if isinstance(v, list):
            out[k] = [str(x)[:300] for x in v[:20]]
        elif isinstance(v, str):
            out[k] = [v[:300]]
    out["biggest_risk"] = str(obj.get("biggest_risk", ""))[:500]
    out["recommendation"] = str(obj.get("recommendation", ""))[:1000]
    return out


# ---------- budget ----------

def _read_budget() -> dict[str, Any]:
    if OPENAI_BUDGET_FILE.exists():
        try:
            return json.loads(OPENAI_BUDGET_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"max": DEFAULT_OPENAI_BUDGET, "used": 0}


def _write_budget(b: dict[str, Any]) -> None:
    OPENAI_BUDGET_FILE.parent.mkdir(parents=True, exist_ok=True)
    OPENAI_BUDGET_FILE.write_text(json.dumps(b), encoding="utf-8")


def reset_openai_budget(max_calls: int = DEFAULT_OPENAI_BUDGET) -> None:
    _write_budget({"max": max_calls, "used": 0})


def _spend_openai(n: int = 1) -> bool:
    b = _read_budget()
    if b.get("used", 0) + n > b.get("max", DEFAULT_OPENAI_BUDGET):
        return False
    b["used"] = int(b.get("used", 0)) + n
    _write_budget(b)
    return True


def openai_budget_status() -> dict[str, Any]:
    return _read_budget()


# ---------- providers ----------

def review_claude_cli(role: dict[str, str], topic: dict[str, Any], evidence: dict[str, Any]) -> dict[str, Any] | None:
    """Invoke `claude -p` on the user's Max-plan auth.

    Requires `claude auth login` to have been run once on this user's machine.
    """
    if not CLAUDE_CLI:
        return None
    pkh = _packet_hash(role["role"], topic, evidence)
    topic_id = topic.get("topic_id", "T?")
    cache_file = _cache_path(role["role"], topic_id, pkh)
    if cache_file.exists():
        try:
            cached = json.loads(cache_file.read_text(encoding="utf-8"))
            cached["from_cache"] = True
            return cached
        except Exception:
            pass

    prompt = _user_prompt(role, topic, evidence)
    cmd = [
        CLAUDE_CLI, "-p",
        "--system-prompt", SYSTEM_PROMPT,
        "--tools", "",
        "--no-session-persistence",
        "--output-format", "json",
        "--model", "haiku",
        "--permission-mode", "bypassPermissions",
    ]
    try:
        proc = subprocess.run(
            cmd, input=prompt, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=180,
        )
        stdout = proc.stdout or ""
        # Outer JSON wrapper has key "result" with the model text
        wrapper = None
        try:
            wrapper = json.loads(stdout)
        except Exception:
            wrapper = None

        if isinstance(wrapper, dict):
            if wrapper.get("is_error") or not wrapper.get("result"):
                msg = str(wrapper.get("result", ""))[:300]
                record_error("claude_cli", role["role"], topic_id, msg or "empty result")
                breadcrumb = LLM_CACHE / "_last_claude_cli_error.json"
                breadcrumb.write_text(json.dumps({
                    "reviewer_role": role["role"], "provider": "claude_cli",
                    "error": True, "message": msg, "topic_id": topic_id,
                }), encoding="utf-8")
                return None
            text = str(wrapper.get("result", ""))
        else:
            text = stdout

        obj = _extract_json(text)
        if obj is None:
            return None
        normalized = _normalize(obj, role["role"])
        normalized["provider"] = "claude_cli"
        cache_file.write_text(json.dumps(normalized), encoding="utf-8")
        return normalized
    except subprocess.TimeoutExpired:
        record_error("claude_cli", role["role"], topic_id, "subprocess timeout")
        return None
    except Exception as e:
        record_error("claude_cli", role["role"], topic_id, f"exception: {e}")
        return None


def review_openai(role: dict[str, str], topic: dict[str, Any], evidence: dict[str, Any]) -> dict[str, Any] | None:
    """Strict tiebreaker. Caller must have already decided to spend a slot."""
    if not have_openai_key():
        return None
    if not _spend_openai(1):
        return _normalize({"recommendation": "openai_budget_exhausted"}, role["role"])
    pkh = _packet_hash(role["role"] + "_openai", topic, evidence)
    topic_id = topic.get("topic_id", "T?")
    cache_file = _cache_path(role["role"] + "_openai", topic_id, pkh)
    if cache_file.exists():
        try:
            return json.loads(cache_file.read_text(encoding="utf-8"))
        except Exception:
            pass
    client = OpenAI()
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=900,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": _user_prompt(role, topic, evidence)},
            ],
        )
        text = resp.choices[0].message.content or ""
        obj = _extract_json(text)
        out = _normalize(obj or {"recommendation": text[:800]}, role["role"])
        out["provider"] = "openai"
        cache_file.write_text(json.dumps(out), encoding="utf-8")
        return out
    except Exception as e:
        record_error("openai", role["role"], topic_id, f"exception: {e}")
        return None


# ---------- inbox fallback ----------

def write_inbox_prompt(role: dict[str, str], topic: dict[str, Any], evidence: dict[str, Any]) -> Path:
    """When no automated provider works, drop a prompt file the user can paste into ChatGPT
    or another local Claude session. Result file expected at the same path with .reply.json."""
    pkh = _packet_hash(role["role"], topic, evidence)
    topic_id = topic.get("topic_id", "T?")
    p = INBOX_DIR / f"{topic_id}_{role['role']}_{pkh}.prompt.txt"
    body = SYSTEM_PROMPT + "\n\n" + _user_prompt(role, topic, evidence)
    p.write_text(body, encoding="utf-8")
    return p


def read_inbox_reply(role: dict[str, str], topic: dict[str, Any], evidence: dict[str, Any]) -> dict[str, Any] | None:
    pkh = _packet_hash(role["role"], topic, evidence)
    topic_id = topic.get("topic_id", "T?")
    p = INBOX_DIR / f"{topic_id}_{role['role']}_{pkh}.reply.json"
    if not p.exists():
        return None
    try:
        return _normalize(json.loads(p.read_text(encoding="utf-8")), role["role"])
    except Exception:
        return None
