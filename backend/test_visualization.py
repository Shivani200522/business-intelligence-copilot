from backend.services.query_service import execute_query
from backend.services.visualization_service import create_bar_chart

query = """
SELECT
    region,
    SUM(quantity * price) AS revenue
FROM sales_dataset
GROUP BY region
ORDER BY revenue DESC
"""

df = execute_query(query)

fig = create_bar_chart(
    df=df,
    x_column="region",
    y_column="revenue",
    title="Revenue by Region"
)

fig.show()