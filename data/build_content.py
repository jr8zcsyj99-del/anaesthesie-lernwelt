"""Load the recovered detailed, source-linked 22-topic edition without shortening it."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
topics=json.loads((ROOT/'data/detailed-topics.json').read_text())
for t in topics:
    t['lessonHtml']=(ROOT/'data/lessons'/f"{t['id']}.html").read_text()
assert len(topics)==22 and len({t['id'] for t in topics})==22
assert all(len(t['cards'])>=20 for t in topics)
assert sum(len(t['cards']) for t in topics)==458
(ROOT/'data/topics.json').write_text(json.dumps(topics,ensure_ascii=False,indent=2))
