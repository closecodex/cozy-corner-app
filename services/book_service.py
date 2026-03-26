from typing import List, Dict
import random
import re

from services.book_data import BOOKS


def search_books(genre: str, keywords: str) -> List[Dict]:
    """
    Return ONLY real books from a local dataset.

    Rules:
    - Exact genre match (case-insensitive) against the book's genres list
    - Optional keyword matching (partial match) against title/author/keywords/description
    - Return 3–5 max
    - If keyword search yields nothing, fall back to random picks from the genre
    """
    genre = (genre or "").strip().lower()
    keywords = (keywords or "").strip().lower()

    if not genre:
        return []

    in_genre = [b for b in BOOKS if genre in [g.lower() for g in b.get("genres", [])]]
    if not in_genre:
        return []

    def normalize(text: str) -> str:
        return re.sub(r"\s+", " ", (text or "").strip().lower())

    tokens = [t for t in re.split(r"[,\s]+", keywords) if t] if keywords else []

    def matches(book: Dict) -> bool:
        hay = " ".join(
            [
                normalize(book.get("title", "")),
                normalize(book.get("author", "")),
                normalize(book.get("description", "")),
                " ".join([normalize(k) for k in book.get("keywords", [])]),
                " ".join([normalize(g) for g in book.get("genres", [])]),
            ]
        )
        return any(t in hay for t in tokens)

    if tokens:
        filtered = [b for b in in_genre if matches(b)]
        if filtered:
            random.shuffle(filtered)
            return [
                {"title": b["title"], "author": b["author"], "description": b["description"]}
                for b in filtered[:5]
            ]

    # Fallback: random picks from the chosen genre
    random.shuffle(in_genre)
    return [
        {"title": b["title"], "author": b["author"], "description": b["description"]}
        for b in in_genre[:5]
    ]

