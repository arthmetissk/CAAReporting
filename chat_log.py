"""Campaign-only chat guardrails and auditable Q&A logging."""

from __future__ import annotations

import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

CHAT_DISCLAIMER = (
    "AI-generated summary — verify figures against the official campaign HTML reports "
    "before decisions. Numbers may be incomplete or paraphrased."
)

# Allowed topical signals for CAA campaign intelligence
_CAMPAIGN_TERMS = [
    "campaign", "promo", "promotion", "loyalty", "offer", "bundle", "combo",
    "may", "june", "july", "august", "2026", "month", "monthly",
    "twinleaf", "smokers", "warehouse", "sw1", "sw2", "txp", "tgc",
    "akwesasne", "covington", "express", "store", "brand",
    "vape", "firework", "fw", "sandwich", "coffee", "bagel", "grab", "food",
    "gng", "zyn", "cooler", "pizza", "gas", "water", "thunder", "spark",
    "beat", "heat", "points", "card", "basket", "revenue", "yoy", "mom",
    "metric", "performance", "result", "summary", "recommend", "recommendation",
    "family", "continuous", "seasonal", "clearance", "redemption", "enrollment",
    "scorecard", "timeline", "arc", "q4", "budget", "roi",
]

_OFF_TOPIC_HINTS = [
    "weather tomorrow", "write code", "python", "javascript", "recipe", "joke",
    "stock tip", "crypto", "bitcoin", "medical advice", "legal advice",
    "who is the president", "sports score", "movie", "dating", "homework",
]

_DB_PATH = Path(__file__).resolve().parent / "data" / "chat_audit.db"


def _connect():
    _DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(_DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_chat_log():
    with _connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS chat_turns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                username TEXT,
                query TEXT NOT NULL,
                answer TEXT,
                formatted_json TEXT,
                metrics_json TEXT,
                campaigns_json TEXT,
                recommendations_json TEXT,
                on_topic INTEGER NOT NULL DEFAULT 1,
                refusal_reason TEXT,
                model_used TEXT,
                useful_for_context INTEGER NOT NULL DEFAULT 1
            )
            """
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_chat_turns_created ON chat_turns(created_at DESC)"
        )
        conn.commit()


def is_campaign_question(query: str) -> tuple[bool, str]:
    """Return (allowed, reason). Fail closed for clearly off-topic prompts."""
    q = (query or "").strip().lower()
    if not q:
        return False, "empty"
    if len(q) > 800:
        return False, "too_long"

    if any(hint in q for hint in _OFF_TOPIC_HINTS):
        return False, "off_topic_hint"

    # Direct campaign lexicon / store keys
    if any(term in q for term in _CAMPAIGN_TERMS):
        return True, "campaign_term"

    # Short follow-ups that still relate when prior context exists are handled by caller;
    # standalone vague prompts without campaign terms are refused.
    if re.fullmatch(r"(hi|hello|hey|thanks|thank you)[.!]?", q):
        return False, "greeting_only"

    return False, "not_campaign_related"


def off_topic_response():
    return {
        "answer": (
            "HEADLINE: This assistant only answers CAA campaign questions.\n"
            "POINTS:\n"
            "- Ask about May–August 2026 campaign performance, stores (SW1/SW2/TXP/TGC), or brands (Twinleaf / Smokers Warehouse).\n"
            "- Ask about continuous families such as sandwich, free coffee, or fireworks.\n"
            "- Ask for recommendations grounded in those campaign reports.\n"
            "NEXT: Rephrase your question around a campaign, month, store, or metric in the reports."
        ),
        "formatted": {
            "headline": "This chat only covers CAA campaign results",
            "context": "Campaign scope only",
            "bullets": [
                "Ask about May–August 2026 performance, recommendations, or continuous families.",
                "Include a month, store (SW1/SW2/TXP/TGC), brand, or campaign name when possible.",
                "General topics outside these campaign reports are out of scope.",
            ],
            "next_step": "Try a campaign question such as “Summarize August results with metrics”.",
        },
        "recommendations": [],
        "metrics": [],
        "campaigns": [],
        "on_topic": False,
        "disclaimer": CHAT_DISCLAIMER,
    }


def log_chat_turn(
    *,
    username: str | None,
    query: str,
    answer: str,
    formatted: dict | None,
    metrics: list | None,
    campaigns: list | None,
    recommendations: list | None,
    on_topic: bool,
    refusal_reason: str | None = None,
    model_used: str | None = None,
):
    init_chat_log()
    with _connect() as conn:
        conn.execute(
            """
            INSERT INTO chat_turns (
                created_at, username, query, answer, formatted_json, metrics_json,
                campaigns_json, recommendations_json, on_topic, refusal_reason, model_used, useful_for_context
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.now(timezone.utc).isoformat(),
                username or "",
                query,
                answer or "",
                json.dumps(formatted or {}, ensure_ascii=False),
                json.dumps(metrics or [], ensure_ascii=False),
                json.dumps(campaigns or [], ensure_ascii=False),
                json.dumps(recommendations or [], ensure_ascii=False),
                1 if on_topic else 0,
                refusal_reason,
                model_used,
                1 if on_topic else 0,
            ),
        )
        conn.commit()


def recent_chat_context(limit: int = 6) -> str:
    """Prior on-topic Q&A for improving continuity (audit-backed memory)."""
    init_chat_log()
    with _connect() as conn:
        rows = conn.execute(
            """
            SELECT query, answer, created_at
            FROM chat_turns
            WHERE on_topic = 1 AND useful_for_context = 1
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    if not rows:
        return ""
    lines = ["Recent audited campaign Q&A (most recent first):"]
    for row in reversed(rows):
        ans = (row["answer"] or "").replace("\n", " ")
        ans = re.sub(r"\s+", " ", ans)[:280]
        lines.append(f"- Q: {row['query'][:180]}")
        lines.append(f"  A: {ans}")
    return "\n".join(lines)


def list_chat_logs(limit: int = 100, on_topic_only: bool = False) -> list[dict]:
    init_chat_log()
    sql = "SELECT * FROM chat_turns"
    if on_topic_only:
        sql += " WHERE on_topic = 1"
    sql += " ORDER BY id DESC LIMIT ?"
    with _connect() as conn:
        rows = conn.execute(sql, (limit,)).fetchall()
    out = []
    for row in rows:
        out.append({
            "id": row["id"],
            "created_at": row["created_at"],
            "username": row["username"],
            "query": row["query"],
            "answer": row["answer"],
            "on_topic": bool(row["on_topic"]),
            "refusal_reason": row["refusal_reason"],
            "model_used": row["model_used"],
            "formatted": json.loads(row["formatted_json"] or "{}"),
            "metrics": json.loads(row["metrics_json"] or "[]"),
            "campaigns": json.loads(row["campaigns_json"] or "[]"),
            "recommendations": json.loads(row["recommendations_json"] or "[]"),
        })
    return out
