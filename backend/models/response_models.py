from pydantic import BaseModel


class AnalyzeResponse(BaseModel):
    data: list
    insights: list[str]

class UploadResponse(BaseModel):
    dataset_id: int
    dataset_name: str
    table_name: str
    rows: int
    columns: int
    message: str