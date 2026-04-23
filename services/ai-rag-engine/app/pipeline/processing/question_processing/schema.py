from typing import List, Literal
from pydantic import BaseModel, Field


class ShariaQuestion(BaseModel):
    question: str = Field(
        ...,
        description="سؤال واضح مستقل بصيغة فصحى بدون ضمائر غامضة"
    )

    type: Literal[
        "حكم", "دليل", "تعليل", "تعريف",
        "تفصيل", "مقارنة", "تطبيق",
        "حالة_شخصية", "استفسار_عام"
    ]

    domain: Literal[
        "فقه", "عقيدة", "سيرة",
        "علوم_القرآن", "حديث",
        "أخلاق", "لغة"
    ]

    is_safe: bool = Field(
        ...,
        description="true إذا كان السؤال مناسب شرعياً"
    )


class QuestionResponse(BaseModel):
    language: Literal["ar"] = "ar"   # 🔥 stricter
    total_questions: int
    questions: List[ShariaQuestion]