#in this file all the logic are written here before importing it in the router file
#logic -> data handling, recieving data, cleaning data, validating data, sending data to the database, getting data from the database, sending response to the client

from src.tasks.dtos import TaskScheme
from sqlalchemy.orm import Session
from src.tasks.models import taskModel
from fastapi import HTTPException

def create_task(body: TaskScheme, db:Session): #bosy is the parameter(variable) whose datatyepe is TaskScheme 
    data = body.model_dump() #convert mmodel into data dictionary
    new_task = taskModel(title = data["title"],      #object gets created of the TaskModel class and stored in the new_task
                         description = data["description"], 
                         is_completed = data["is_completed"])
    db.add(new_task)
    db.commit()
    db.refresh(new_task) #refresh helps to get the updated version of the data for example id was not therehence it created it and updated it hence the updated version of the database is present in the new_task

    return new_task

def get_tasks(db:Session):
    tasks = db.query(taskModel).all()
    return tasks

# def get_task_byId(task_id:int, db:Session):
#     tasks = db.query(taskModel).all()

#     for task in tasks:
#         if task.id == task_id:
#             return task

def get_task_byID(task_id:int, db:Session):
    task = db.query(taskModel).get(task_id)

    if not task: 
        raise HTTPException(404, detail = "Task id is incorrect")
    
    return task

def update_task(body:TaskScheme, task_id:int, db:Session):
    task = db.query(taskModel).get(task_id)

    if not task:
        raise HTTPException(404, detail = "Task id is incorrect")
    
    # task.title = body.title
    # task.description = body.description
    # task.is_completed = body.is_completed

    body = body.model_dump()
    for field, value in body.items():
        setattr(task, field, value)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def delete_task(task_id : int, db:Session):
    task = db.query(taskModel).get(task_id)

    if not task:
        raise HTTPException(404, detail = "task not found")
    
    db.delete(task)
    db.commit()
    return None

    #return {"status" : "Task deleted successfully"}  #delete does not have any status return type hence we return none instead
