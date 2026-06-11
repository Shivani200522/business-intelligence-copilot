from backend.services.analysis_service import (
    analyze_query
)

query = """
SELECT
    region,
    SUM(quantity * price) AS revenue
FROM sales_dataset
GROUP BY region
ORDER BY revenue DESC
"""

result = analyze_query(query)

print("\nINSIGHTS:\n")

for insight in result["insights"]:
    print("-", insight)

result["chart"].show()