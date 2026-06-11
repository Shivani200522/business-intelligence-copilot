from backend.services.query_service import execute_query

from backend.services.chart_selector_service import (
    select_chart_type
)

from backend.services.visualization_service import (
    create_visualization
)

from backend.services.insight_service import (
    generate_insights
)


def analyze_query(sql_query):

    df = execute_query(sql_query)

    chart_type = select_chart_type(df)

    fig = create_visualization(
        df=df,
        chart_type=chart_type,
        title="Analysis Result"
    )

    insights = generate_insights(df)

    return {
        "data": df,
        "chart": fig,
        "insights": insights
    }