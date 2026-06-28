def generate_insights(df):

    if df is None or len(df) == 0:
        return ["No data available"]

    insights = []

    # try simple numeric column detection
    numeric_cols = df.select_dtypes(include=["number"]).columns

    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        insights.append(f"Average {col}: {df[col].mean():.2f}")
        insights.append(f"Max {col}: {df[col].max()}")
        insights.append(f"Min {col}: {df[col].min()}")

    insights.append(f"Total rows: {len(df)}")

    return insights