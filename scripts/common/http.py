"""
Cached HTTP GET with retries, polite rate limiting, and on-disk SQLite cache.
Stdlib only.
"""
from __future__ import annotations
import hashlib
import json
import sqlite3
import time
import urllib.parse
import urllib.request
import urllib.error
import gzip
import io
from pathlib import Path
from typing import Any

DEFAULT_TIMEOUT = 30
DEFAULT_TTL_SECONDS = 7 * 24 * 3600  # 7 days
USER_AGENT = "research-command-center/0.1 (private; contact: local user)"

REPO_ROOT = Path(__file__).resolve().parents[2]
CACHE_DB = REPO_ROOT / "data" / "cache" / "http_cache.sqlite"
LOG_DIR = REPO_ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DB.parent.mkdir(parents=True, exist_ok=True)


def _conn() -> sqlite3.Connection:
    c = sqlite3.connect(CACHE_DB)
    c.execute(
        "CREATE TABLE IF NOT EXISTS cache ("
        "key TEXT PRIMARY KEY, url TEXT, fetched_at INTEGER, status INTEGER, body BLOB)"
    )
    return c


def _key(url: str, params: dict[str, Any] | None) -> str:
    norm = url + "?" + urllib.parse.urlencode(sorted((params or {}).items()))
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def _log(line: str) -> None:
    with open(LOG_DIR / "http.log", "a", encoding="utf-8") as f:
        f.write(f"{int(time.time())}\t{line}\n")


_LAST_HOST_CALL: dict[str, float] = {}


def _host(url: str) -> str:
    return urllib.parse.urlparse(url).netloc


def _rate_limit(url: str, min_interval: float) -> None:
    h = _host(url)
    last = _LAST_HOST_CALL.get(h, 0.0)
    delta = time.time() - last
    if delta < min_interval:
        time.sleep(min_interval - delta)
    _LAST_HOST_CALL[h] = time.time()


def get(
    url: str,
    params: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    *,
    ttl: int = DEFAULT_TTL_SECONDS,
    min_interval: float = 1.1,
    retries: int = 3,
    timeout: int = DEFAULT_TIMEOUT,
) -> tuple[int, str]:
    """
    Cached HTTP GET. Returns (status_code, body_text).
    On cache hit returns cached value if fresher than ttl.
    On network/HTTP errors retries with exponential backoff.
    """
    full = url + ("?" + urllib.parse.urlencode(params) if params else "")
    k = _key(url, params)
    now = int(time.time())

    conn = _conn()
    row = conn.execute(
        "SELECT fetched_at, status, body FROM cache WHERE key=?", (k,)
    ).fetchone()
    if row and (now - int(row[0])) < ttl:
        body = row[2]
        if isinstance(body, bytes):
            body = body.decode("utf-8", errors="replace")
        _log(f"CACHE_HIT\t{full}")
        return int(row[1]), body

    last_err = None
    for attempt in range(retries):
        try:
            _rate_limit(url, min_interval)
            req = urllib.request.Request(full)
            req.add_header("User-Agent", USER_AGENT)
            req.add_header("Accept-Encoding", "gzip")
            for hk, hv in (headers or {}).items():
                req.add_header(hk, hv)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.GzipFile(fileobj=io.BytesIO(raw)).read()
                body = raw.decode("utf-8", errors="replace")
                status = r.status
                conn.execute(
                    "INSERT OR REPLACE INTO cache(key,url,fetched_at,status,body) VALUES(?,?,?,?,?)",
                    (k, full, now, status, body.encode("utf-8")),
                )
                conn.commit()
                _log(f"FETCH\t{status}\t{full}")
                return status, body
        except urllib.error.HTTPError as e:
            last_err = e
            _log(f"HTTP_ERR\t{e.code}\t{full}\t{e.reason}")
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt)
                continue
            # cache the error so we don't retry forever
            try:
                body = e.read().decode("utf-8", errors="replace") if hasattr(e, "read") else ""
            except Exception:
                body = ""
            return e.code, body
        except urllib.error.URLError as e:
            last_err = e
            _log(f"URL_ERR\t{full}\t{e.reason}")
            time.sleep(2 ** attempt)
        except Exception as e:
            last_err = e
            _log(f"EXC\t{full}\t{type(e).__name__}\t{e}")
            time.sleep(2 ** attempt)

    return 0, f"ERROR after {retries} retries: {last_err}"


def get_json(
    url: str,
    params: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    **kwargs: Any,
) -> tuple[int, Any]:
    status, body = get(url, params, headers, **kwargs)
    if status >= 400 or not body:
        return status, None
    try:
        return status, json.loads(body)
    except Exception:
        return status, None
