from typing import Optional

from pydantic import BaseModel 


class Answer_Response(BaseModel) : 
    id: str
    text: str
    source: str
    book: Optional[str] = None
    chapter: Optional[str] = None
    score: float
    rerank_score: Optional[float] = None


class ExtractedText(BaseModel):
    text: str
    source: str


class AnswerResponse(BaseModel):
    results: list[ExtractedText]
    is_answered: bool
