import plotly.express as px


def create_visualization(df, chart_type, title):

    columns = list(df.columns)

    x_col = columns[0]
    y_col = columns[1]

    if chart_type == "bar":

        return px.bar(
            df,
            x=x_col,
            y=y_col,
            title=title
        )

    elif chart_type == "line":

        return px.line(
            df,
            x=x_col,
            y=y_col,
            title=title
        )

    elif chart_type == "pie":

        return px.pie(
            df,
            names=x_col,
            values=y_col,
            title=title
        )

    return None