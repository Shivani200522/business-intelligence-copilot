from fastapi import APIRouter

from backend.models.request_models import AnalyzeRequest
from backend.models.response_models import AnalyzeResponse

from backend.services.analysis_service import (
    analyze_query
)

router = APIRouter()


@router.get("/")
def home():

    return {
        "message": "Business Intelligence Copilot API Running"
    }


@router.post(
    "/analyze",
    response_model=AnalyzeResponse
)
def analyze(request: AnalyzeRequest):

    result = analyze_query(
        request.sql_query
    )

    return {
        "data": result["data"].to_dict(
            orient="records"
        ),
        "insights": result["insights"]
    }