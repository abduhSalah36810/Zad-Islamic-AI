
import os 
import json 
from openai import OpenAI 
from dotenv import load_dotenv
load_dotenv()

import os
import json
import re
from openai import OpenAI

class LLMClient: 
    def __init__(self, model: str = "openai/gpt-4o-mini"):
        api_key = os.getenv("OPEN_AI_KEY")
        self.client = OpenAI(base_url="https://models.github.ai/inference",
                             api_key=api_key) 
        self.model = model
         
    def generate(self, prompt: str, temperature: float = 0.2) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "أنت مساعد دقيق."},
                {"role": "user", "content": prompt},
            ], 
            temperature=temperature,
            max_tokens=4096,
            top_p=1
        )
        return response.choices[0].message.content 

    def generate_json(self, prompt: str, temperature: float = 0.2) -> dict:
        response_text = self.generate(prompt, temperature)

        # If already a dict, just return it
        if isinstance(response_text, dict):
            return response_text

        # Remove Markdown code block if present
        cleaned_text = re.sub(r"^```json\s*|```$", "", response_text.strip(), flags=re.MULTILINE)

        # Try to parse JSON
        try:
            return json.loads(cleaned_text)
        except json.JSONDecodeError:
            # Optional: fallback to searching JSON inside text
            match = re.search(r"\{.*\}", cleaned_text, re.DOTALL)
            if match:
                return json.loads(match.group())
            raise ValueError(f"LLM did not return valid JSON: {response_text}")