import pandas as pd

from sqlalchemy import text

from backend.database.connection import engine


def load_dataset(file_path: str):
    df = pd.read_csv(file_path)

    print("\nDataset Loaded Successfully\n")

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nPreview:")
    print(df.head())

    return df


def get_next_table_name():
    query = text("""
        SELECT COUNT(*) FROM datasets;
    """)

    with engine.begin() as connection:
        total = connection.execute(query).scalar()

    return f"dataset_{total + 1}"


def register_dataset(file_name: str, table_name: str):

    # after inserting into DB
    dataset_id = result.scalar()

    return {
        "dataset_id": dataset_id,
        "dataset_name": file_name,
        "table_name": table_name
    }