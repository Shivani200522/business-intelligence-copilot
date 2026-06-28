from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    sql_query: str