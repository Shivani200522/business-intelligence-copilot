from backend.services.query_service import execute_query

from backend.services.chart_selector_service import (
    select_chart_type
)

from backend.services.visualization_service import (
    create_visualization
)

query = """
SELECT
    region,
    SUM(quantity * price) AS revenue
FROM sales_dataset
GROUP BY region
"""

df = execute_query(query)

chart_type = select_chart_type(df)

print("Selected Chart:", chart_type)

fig = create_visualization(
    df,
    chart_type,
    "Revenue By Region"
)

fig.show()