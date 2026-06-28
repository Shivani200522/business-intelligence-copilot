from pydantic import BaseModel


class AnalyzeResponse(BaseModel):
    data: list
    insights: list[str]