from pprint import pprint

from backend.services.dataset_service import load_dataset
from backend.services.profiler_service import profile_dataset

df = load_dataset("sample_data/sales.csv")

profile = profile_dataset(df)

pprint(profile)