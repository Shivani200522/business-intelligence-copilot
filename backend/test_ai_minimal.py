from backend.ai.ai_service import AIService

ai = AIService()

print(ai.generate_sql(
    question="Show revenue by region",
    table_name="sales_dataset",
    schema=["region", "price", "quantity"]
))