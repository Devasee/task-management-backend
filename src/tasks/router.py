#define router here
from fastapi import APIRouter, Depends,status
from src.tasks import controller
from src.tasks.dtos import TaskScheme, TaskResponseScheme
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session

task_routes = APIRouter(prefix = "/tasks") #helps to define the routes for the task management app
 
@task_routes.post("/create", response_model=TaskResponseScheme, status_code = status.HTTP_201_CREATED) #instead of app.post we will be using task_routes
def create_task(body: TaskScheme, db:Session = Depends(get_db)): #here db paramter help to get the databse using the db_get() function
    return controller.create_task(body, db)

@task_routes.get("/all_tasks", response_model = List[TaskResponseScheme], status_code=status.HTTP_200_OK)
def get_all_tasks(db:Session = Depends(get_db)):
    return controller.get_tasks(db)

@task_routes.get("/one_task/{task_id}", response_model=TaskResponseScheme, status_code=status.HTTP_200_OK)
def get_task_byId(task_id: int, db:Session = Depends(get_db)):
    return controller.get_task_byID(task_id, db)

@task_routes.post("/update_task/{task_id}",response_model=TaskResponseScheme, status_code=status.HTTP_200_OK)
def update_task(body:TaskScheme, task_id:int, db:Session=Depends(get_db)):
    return controller.update_task(body, task_id, db)

@task_routes.delete("/delete_task/{task_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_task_byID(task_id: int, db:Session = Depends(get_db)):
    return controller.delete_task(task_id, db)