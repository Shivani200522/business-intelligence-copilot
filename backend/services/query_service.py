import pandas as pd

from sqlalchemy import text

from backend.database.connection import engine


def execute_query(sql_query: str):

    with engine.connect() as connection:

        result = pd.read_sql(
            text(sql_query),
            connection
        )

    return result