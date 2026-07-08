#they need to pass the username password of the user
from pydantic import BaseModel

class userSchema(BaseModel):
    name : str
    username : str
    password : str
    email : str
    mobile : str

class userResponseSchema(BaseModel):
    id : int
    name : str
    username : str
    email : str
    mobile : str

class loginSchema(BaseModel):
    username : str
    password : str

