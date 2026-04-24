from typing import List
from .schema import Chunk


def format_context(chunks: List[Chunk]) -> str:
    blocks = []

    for c in chunks:
        block = f"""[ID: {c.id}]
[المصدر: {c.source} | الكتاب: {c.book or "غير محدد"} | الباب: {c.chapter or "غير محدد"}]
النص: {c.text}
"""
        blocks.append(block)

    return "\n\n".join(blocks)