from backend.services.query_service import execute_query

from backend.services.insight_service import generate_insights


query = """
SELECT
    region,
    SUM(quantity * price) AS revenue
FROM sales_dataset
GROUP BY region
ORDER BY revenue DESC
"""

df = execute_query(query)

insights = generate_insights(df)

for insight in insights:
    print(insight)