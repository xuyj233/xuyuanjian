from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

ROOT = Path(__file__).resolve().parents[1]
TEX_PATH = ROOT / "source" / "resume.tex"
OUTPUT_PATH = ROOT / "data" / "publications.json"


@dataclass
class Publication:
    title: str
    authors: str
    venue: Optional[str] = None
    note: Optional[str] = None
    year: Optional[int] = None

    def to_dict(self) -> dict:
        data = asdict(self)
        return {key: value for key, value in data.items() if value}


def clean_tex(text: str) -> str:
    """Simplify LaTeX markup to plain text."""
    replacements = [
        (r"``", '"'),
        (r"''", '"'),
        (r"---", "—"),
        (r"--", "–"),
    ]
    for pattern, repl in replacements:
        text = text.replace(pattern, repl)

    # Replace simple commands
    simple_commands = [
        r"textbf",
        r"myemph",
        r"textnormal",
    ]
    for cmd in simple_commands:
        text = re.sub(rf"\\{cmd}\{{([^{{}}]+)\}}", r"\1", text)

    text = re.sub(r"\\href\{([^{}]+)\}\{([^{}]+)\}", r"\2", text)
    text = text.replace(r"\&", "&").replace(r"\%", "%")
    text = re.sub(r"\\[a-zA-Z]+\s*", "", text)  # drop remaining commands
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_section(tex: str, section: str) -> List[Publication]:
    pattern = rf"\\section\{{{re.escape(section)}\}}(?P<body>.*?\\end\{{itemize\}})"
    match = re.search(pattern, tex, flags=re.DOTALL)
    if not match:
        return []

    block = match.group("body")
    block = re.sub(r"\\begin\{itemize\}(?:\[[^\]]*\])?", "", block, count=1, flags=re.DOTALL)
    block = re.sub(r"\\setlength\\itemsep\{[^{}]*\}", "", block)
    block = re.sub(r"\\end\{itemize\}", "", block, count=1)
    items = re.split(r"\\item", block)

    publications: List[Publication] = []
    for raw in items:
        raw = raw.strip()
        if not raw:
            continue
        entry = clean_tex(raw)
        if not entry:
            continue
        publications.append(parse_entry(entry))

    return publications


def parse_entry(entry: str) -> Publication:
    title_match = re.search(r'"([^"]+)"', entry)
    if not title_match:
        return Publication(title=entry, authors="")

    title = title_match.group(1).strip()
    before = entry[: title_match.start()].strip().rstrip(".,; ")
    after = entry[title_match.end() :].strip().lstrip(". ").strip()

    authors = before
    venue = None
    note = None
    year = None

    if after:
        lower_after = after.lower()
        cleaned = after.rstrip(".")
        if after.lower().startswith("in "):
            if lower_after.startswith("in preparation"):
                note = cleaned
            else:
                venue = cleaned
        else:
            note = cleaned

    if venue:
        year_match = re.search(r"(19|20)\d{2}", venue)
        if year_match:
            year = int(year_match.group(0))

    return Publication(title=title, authors=authors, venue=venue, note=note, year=year)


def build_payload(tex: str) -> dict:
    published = parse_section(tex, "Published Papers")
    ongoing = parse_section(tex, "Ongoing Papers")

    payload = {
        "generated_at": datetime.now(tz=timezone.utc).isoformat(),
        "published": [pub.to_dict() for pub in published],
        "ongoing": [pub.to_dict() for pub in ongoing],
        "counts": {
            "published": len(published),
            "ongoing": len(ongoing),
        },
    }
    return payload


def main() -> None:
    if not TEX_PATH.exists():
        raise FileNotFoundError(f"LaTeX resume not found at {TEX_PATH}")

    tex = TEX_PATH.read_text(encoding="utf-8")
    payload = build_payload(tex)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {OUTPUT_PATH.relative_to(ROOT)} with {payload['counts']['published']} published and {payload['counts']['ongoing']} ongoing papers.")


if __name__ == "__main__":
    main()

