import json
import logging
from string import Template
from .prompt import COMBINED_QUESTION_PROMPT
from .schema import QuestionResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Question_Processor:
    def __init__(self, llm):
        self.llm = llm

    def run(self, text: str):
        # 1. build prompt
        prompt = Template(COMBINED_QUESTION_PROMPT).substitute(text=text)

        # 2. call LLM
        raw_output = self.llm.generate_json(prompt)

        logger.info(f"RAW OUTPUT: {raw_output}")

        # 3. safe parse
        data = self._safe_json_parse(raw_output)

        logger.info(f"PARSED DATA: {data}")

        # 4. normalize (🔥 مهم جدًا)
        data = self._normalize(data)

        try:
            validated = QuestionResponse.model_validate(data)

            return [q.model_dump() for q in validated.questions]

        except Exception as e:
            logger.error(f"Validation failed. Data: {data}")
            logger.error(f"Error: {e}")
            return []

    def _safe_json_parse(self, raw_output):
        if isinstance(raw_output, dict):
            return raw_output

        try:
            clean_output = str(raw_output).strip()

            if clean_output.startswith("```"):
                clean_output = clean_output.replace("```json", "").replace("```", "").strip()

            return json.loads(clean_output)

        except json.JSONDecodeError as e:
            logger.error(f"JSON Parsing Error: {e}")
            return {"questions": []}

    def _normalize(self, data: dict) -> dict:
        # 🔧 fix missing total_questions
        if "total_questions" not in data:
            data["total_questions"] = len(data.get("questions", []))

        # 🔧 fix structure
        for q in data.get("questions", []):
            # type fix
            if "question_type" in q:
                q["type"] = q.pop("question_type")

            # domain fix
            if q.get("domain") == "لغة_شرعية":
                q["domain"] = "لغة"

            # fallback defaults (optional but safe)
            if "type" not in q:
                q["type"] = "استفسار_عام"

            if "domain" not in q:
                q["domain"] = "فقه"

            if "is_safe" not in q:
                q["is_safe"] = True

        return data