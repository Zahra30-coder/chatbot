from app.database.db import engine
from app.database.models import Base

#python -m app.database.init_db

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created")
print(Base.metadata.tables.keys())