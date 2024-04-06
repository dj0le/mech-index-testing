from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DATABASE_URL = "sqlite:///./mwomechs.db"

engine = create_engine(
    SQL_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()








# from sqlmodel import SQLModel, create_engine

# sqlite_file_name = "mwomechs.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url)

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

    