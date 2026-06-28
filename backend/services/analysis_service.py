from backend.ai.ai_service import AIService
from backend.services.query_service import execute_query
from backend.services.insight_service import generate_insights


def analyze_question(question: str, table_name: str, schema: list):

    ai = AIService()

    sql = ai.generate_sql(
        question=question,
        table_name=table_name,
        schema=schema,
    )

    print("\n[GENERATED SQL]\n", sql)

    # 🔥 SAFE EXECUTION (prevents 500 crash)
    try:
        data = execute_query(sql)
    except Exception as e:
        return {
            "question": question,
            "sql": sql,
            "data": [],
            "insights": [f"SQL Execution Error: {str(e)}"]
        }

    try:
        insights = generate_insights(data)
    except Exception as e:
        insights = [f"Insight generation error: {str(e)}"]

    return {
        "question": question,
        "sql": sql,
        "data": data.to_dict(orient="records") if hasattr(data, "to_dict") else [],
        "insights": insights,
    }