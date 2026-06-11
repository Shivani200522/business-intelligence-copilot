from sqlalchemy import create_engine
from sqlalchemy import text

import pandas as pd

from backend.database.connection import engine


def load_dataframe_to_postgres(
    df: pd.DataFrame,
    table_name: str
):

    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"✅ Table '{table_name}' created successfully")