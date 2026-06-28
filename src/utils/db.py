from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.settings import settings

Base = declarative_base()

engine = create_engine(url = settings.DB_CONNECTION)

LocalSession = sessionmaker(bind = engine)

#whenever i have the requirement we can get this session(whenever we connect with db and do some queries I should atlease one object)
def get_db():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()