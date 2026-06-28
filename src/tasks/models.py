#helps to define database tables
from sqlalchemy import Column, Integer, String , Boolean
from src.utils.db import Base #helps to connect tables /models to te actual database

class taskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key = True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default = False)
