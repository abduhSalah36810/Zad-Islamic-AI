import json
from .schema import AnswerResponse, ExtractedText


def parse_output(text: str) -> AnswerResponse:
    try:
        data = json.loads(text)

        results = [
            ExtractedText(
                text=item["text"],
                source=item["source"]
            )
            for item in data.get("results", [])
        ]

        return AnswerResponse(
            results=results,
            is_answered=data.get("is_answered", False)
        )

    except Exception:
        return AnswerResponse(results=[], is_answered=False)