#they need to pass the usename password of the user
#schema of the body is defined here

from pydantic import BaseModel

class TaskScheme(BaseModel): 
    title:str
    description:str
    is_completed:bool = False

#created so that the response body contains only that much data we want to make the user see 
#for example - password, secret keys etc
class TaskResponseScheme(BaseModel):
    id:int
    title : str
    description:str
    is_completed:bool
