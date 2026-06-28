from backend.ai.ai_service import AIService

ai = AIService()

sql = ai.generate_sql(
    question="Show total revenue by region",
    table_name="sales_dataset",
    schema=[
        "date",
        "product",
        "quantity",
        "price",
        "region",
    ],
)

print("\nGenerated SQL:\n")
print(sql)