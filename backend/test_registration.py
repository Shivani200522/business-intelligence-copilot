from backend.services.dataset_service import load_dataset
from backend.services.profiler_service import profile_dataset
from backend.services.registration_service import register_dataset

from backend.database.connection import SessionLocal

db = SessionLocal()

df = load_dataset("sample_data/sales.csv")

profile = profile_dataset(df)

dataset_id = register_dataset(
    db=db,
    dataset_name="sales_dataset",
    file_name="sales.csv",
    profile=profile
)

print(f"\nDataset Registered Successfully")
print(f"Dataset ID: {dataset_id}")