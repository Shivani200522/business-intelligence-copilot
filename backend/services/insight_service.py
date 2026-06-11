def generate_insights(df):

    insights = []

    columns = list(df.columns)

    if len(columns) != 2:
        return [
            "Unable to generate insights for this result structure."
        ]

    category_col = columns[0]
    metric_col = columns[1]

    total = df[metric_col].sum()

    top = df.iloc[0]
    bottom = df.iloc[-1]

    top_share = (
        top[metric_col] / total
    ) * 100

    difference = (
        (top[metric_col] - bottom[metric_col])
        / top[metric_col]
    ) * 100

    insights.append(
        f"{top[category_col]} has the highest {metric_col}."
    )

    insights.append(
        f"{top[category_col]} contributes {top_share:.1f}% of total {metric_col}."
    )

    insights.append(
        f"{bottom[category_col]} is the lowest performer."
    )

    insights.append(
        f"The gap between top and bottom performers is {difference:.1f}%."
    )

    return insights