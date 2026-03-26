import sqlite3
from typing import List
import random


THEMES = [
    "A sleepy cat in a sunbeam",
    "A stack of favorite books",
    "A tiny cafe on a rainy street",
    "A cozy corner full of pillows",
    "A plant that is thriving a little too hard",
    "A dog dreaming about adventures",
    "A messy but lovable desk",
]

STYLES = [
    "soft watercolor",
    "bold comic lines",
    "minimalist shapes",
    "pastel chalk",
    "pixel art",
    "ink sketch",
]

CONSTRAINTS = [
    "only 2 colors",
    "no straight lines",
    "everything must float",
    "tiny stars hidden everywhere",
    "no faces, only silhouettes",
    "fit inside a perfect square",
]


def init_db(path: str) -> None:
    conn = sqlite3.connect(path)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS drawing_prompts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt_date TEXT NOT NULL,
                prompt_text TEXT NOT NULL
            )
            """
        )
        conn.commit()
    finally:
        conn.close()


def generate_prompt() -> str:
    """Create a cozy, slightly silly drawing prompt."""
    theme = random.choice(THEMES)
    style = random.choice(STYLES)
    constraint = random.choice(CONSTRAINTS)
    return f"Draw {theme} in a {style} style, using {constraint}."


def save_prompt_if_new(path: str, prompt_date: str, prompt_text: str) -> None:
    conn = sqlite3.connect(path)
    try:
        cur = conn.execute(
            "SELECT id FROM drawing_prompts WHERE prompt_date = ? AND prompt_text = ?",
            (prompt_date, prompt_text),
        )
        if cur.fetchone() is None:
            conn.execute(
                "INSERT INTO drawing_prompts (prompt_date, prompt_text) VALUES (?, ?)",
                (prompt_date, prompt_text),
            )
            conn.commit()
    finally:
        conn.close()


def get_recent_prompts(path: str, limit: int = 5, only_today: bool = False) -> List[str]:
    conn = sqlite3.connect(path)
    try:
        if only_today:
            cur = conn.execute(
                "SELECT prompt_text FROM drawing_prompts ORDER BY id DESC LIMIT 1"
            )
        else:
            cur = conn.execute(
                "SELECT prompt_text FROM drawing_prompts ORDER BY id DESC LIMIT ?",
                (limit,),
            )
        rows = cur.fetchall()
        return [r[0] for r in rows]
    except sqlite3.OperationalError:
        return []
    finally:
        conn.close()
    return []

