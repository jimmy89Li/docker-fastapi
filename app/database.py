from sqlmodel import SQLModel, create_engine
from contextlib import asynccontextmanager

# Database engine
sqlite_file_name = "address_book.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


@asynccontextmanager
async def lifespan(app):
    create_db_and_tables()
    yield


# Create database tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
