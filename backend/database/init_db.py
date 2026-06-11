from backend.database.connection import engine
from backend.database.base import Base

import backend.database.models

Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully")