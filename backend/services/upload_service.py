import pandas as pd

from backend.database.connection import engine
from backend.services.dataset_service import (
    get_next_table_name,
    register_dataset,
)


def upload_dataset(file):
    """
    Handles the complete dataset upload workflow.
    """

    df = pd.read_csv(file.file)

    table_name = get_next_table_name()

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False,
    )

    dataset_id = register_dataset(
        dataset_name=file.filename,
        table_name=table_name,
        rows=len(df),
        columns=len(df.columns),
    )

    return {
        "dataset_id": dataset_id,
        "dataset_name": file.filename,
        "table_name": table_name,
        "rows": len(df),
        "columns": len(df.columns),
        "message": "Dataset uploaded successfully",
    }