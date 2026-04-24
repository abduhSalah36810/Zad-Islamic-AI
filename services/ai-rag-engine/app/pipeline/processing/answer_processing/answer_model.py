from typing import List
from .schema import Chunk, AnswerResponse
from .formatter import format_context
from .prompt_builder import build_prompt
from models.LLM.client import LLMClient
from .parser import parse_output


def answer_question(question: str, chunks: List[Chunk]) -> AnswerResponse:

    # 1. ترتيب واختيار أفضل chunks
    chunks = sorted(
        chunks,
        key=lambda x: x.rerank_score or x.score,
        reverse=True
    )[:5]

    # 2. بناء السياق
    context = format_context(chunks)

    # 3. بناء البرومبت
    prompt = build_prompt(question, context)

    # 4. استدعاء الموديل
    raw_output = LLMClient.generate_json(prompt)

    # 5. parsing
    parsed = parse_output(raw_output)

    return parsed