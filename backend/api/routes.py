from fastapi import APIRouter, UploadFile, File
import pandas as pd
import time

from sqlalchemy import text

from backend.database.connection import engine
from backend.state import LAST_DATASET

from backend.services.analysis_service import analyze_question

from backend.models.request_models import AnalyzeRequest
from backend.models.response_models import AnalyzeResponse, UploadResponse

router = APIRouter()


@router.get("/")
def home():

    return {
        "message": "Business Intelligence Copilot API Running"
    }


from backend.models.request_models import AnalyzeRequest
from backend.models.response_models import AnalyzeResponse
from backend.services.analysis_service import analyze_question


from backend.state import LAST_DATASET
from backend.services.analysis_service import analyze_question


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):

    table_name = LAST_DATASET["table_name"]
    schema = LAST_DATASET["schema"]

    if not table_name:
        return {
            "data": [],
            "insights": ["No dataset uploaded yet"]
        }

    result = analyze_question(
        question=request.question,
        table_name=table_name,
        schema=schema,
    )

    return result


@router.post("/upload", response_model=UploadResponse)
def upload_dataset(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    table_name = f"dataset_{int(time.time())}"

    df.to_sql(table_name, engine, if_exists="replace", index=False)

    # fetch schema
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM {table_name} LIMIT 1"))
        schema = list(result.keys())

    LAST_DATASET["table_name"] = table_name
    LAST_DATASET["schema"] = schema

    return {
        "dataset_id": 0,
        "dataset_name": file.filename,
        "table_name": table_name,
        "rows": len(df),
        "columns": len(df.columns),
        "message": "Dataset uploaded successfully"
    }