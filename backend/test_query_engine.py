from backend.services.query_service import execute_query

query = """
SELECT
    region,
    SUM(quantity * price) AS revenue
FROM sales_dataset
GROUP BY region
ORDER BY revenue DESC
"""

result = execute_query(query)

print(result)