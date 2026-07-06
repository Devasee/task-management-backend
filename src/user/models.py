#helps to define database tables
from sqlalchemy import Column, Integer, String
from src.utils.db import Base

class userModel(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable = False)
    email = Column(String, unique=True)
    mobile = Column(String)

