"""
JSON / CSV helpers and a tiny logger.
"""
from __future__ import annotations
import csv
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Iterable

REPO_ROOT = Path(__file__).resolve().parents[2]
LOG_DIR = REPO_ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, default=str)


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def read_csv(path: Path) -> list[dict[str, str]]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, Any]], header: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        if header:
            with open(path, "w", encoding="utf-8", newline="") as f:
                csv.writer(f).writerow(header)
        return
    fields = header or list(rows[0].keys())
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


def log(stream: str, msg: str) -> None:
    line = f"{int(time.time())}\t{stream}\t{msg}"
    sys.stderr.write(line + "\n")
    with open(LOG_DIR / "pipeline.log", "a", encoding="utf-8") as f:
        f.write(line + "\n")


def topic_dir(rel: str, topic_id: str) -> Path:
    p = REPO_ROOT / rel / topic_id
    p.mkdir(parents=True, exist_ok=True)
    return p


def evidence_dir(topic_id: str) -> Path:
    return topic_dir("data/evidence", topic_id)
