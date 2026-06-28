from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    question: str