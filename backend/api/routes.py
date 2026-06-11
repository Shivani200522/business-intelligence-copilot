from fastapi import APIRouter

from backend.services.analysis_service import (
    analyze_query
)

router = APIRouter()


@router.get("/")
def home():

    return {
        "message": "Business Intelligence Copilot API Running"
    }


@router.post("/analyze")
def analyze(sql_query: str):

    result = analyze_query(sql_query)

    return {
        "data": result["data"].to_dict(
            orient="records"
        ),
        "insights": result["insights"]
    }