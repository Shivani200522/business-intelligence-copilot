from backend.services.dataset_service import load_dataset
from backend.services.table_loader_service import load_dataframe_to_postgres

df = load_dataset(
    "sample_data/sales.csv"
)

load_dataframe_to_postgres(
    df=df,
    table_name="sales_dataset"
)