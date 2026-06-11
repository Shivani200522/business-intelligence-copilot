from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from backend.database.base import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    file_name = Column(String, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )