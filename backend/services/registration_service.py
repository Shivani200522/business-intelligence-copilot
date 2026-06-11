import json

from sqlalchemy.orm import Session

from backend.database.models import Dataset
from backend.database.models import DatasetProfile


def register_dataset(
    db: Session,
    dataset_name: str,
    file_name: str,
    profile: dict
):

    dataset = Dataset(
        name=dataset_name,
        file_name=file_name
    )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    dataset_profile = DatasetProfile(
        dataset_name=dataset_name,
        schema_json=json.dumps(profile)
    )

    db.add(dataset_profile)
    db.commit()

    return dataset.id