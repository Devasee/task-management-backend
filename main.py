from fastapi import FastAPI
from src.utils.settings import settings
from src.utils.db import Base, engine
from src.tasks.router import task_routes

Base.metadata.create_all(engine) #whenever the system or server starts it will try to connect to the database and if connected successfully then the tables presented in the project get created in database

app = FastAPI(title = "Task Management App")
app.include_router(task_routes)