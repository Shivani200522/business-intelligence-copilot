def select_chart_type(df):

    columns = list(df.columns)

    if len(columns) != 2:
        return "table"

    first_col = columns[0]

    if "date" in first_col.lower():
        return "line"

    return "bar"