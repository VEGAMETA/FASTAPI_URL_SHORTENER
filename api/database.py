from sqlalchemy import Engine, create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from databases import Database
from api.models import Base

DATABASE_URL = "sqlite:///./database/links.sqlite"

database: Database = Database(DATABASE_URL)
metadata: MetaData = MetaData()
engine: Engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal: sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
