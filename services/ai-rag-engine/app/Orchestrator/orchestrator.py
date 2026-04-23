
from app.models.LLM.client import LLMClient
from app.pipeline.processing.question_processing.question_model import Question_Processor
class AIOrchestrator : 
    def __init__(self) : 
        self.llm = LLMClient()
        self.question_model = Question_Processor(self.llm)

    def process(self , text : str ) : 
        return self.question_model.run(text)