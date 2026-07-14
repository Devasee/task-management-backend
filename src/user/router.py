#define router here

from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.orm import Session
from src.user.dtos import userSchema, userResponseSchema, loginSchema
from src.utils.db import get_db
from src.user import controller

user_routes = APIRouter(prefix = "/user")

#we have use the response model as we want to return the specific details only from the user  i.e we dont want to return the password / even hashpassword
@user_routes.post("/register", response_model=userResponseSchema, status_code = status.HTTP_201_CREATED)
def register(body:userSchema, db:Session = Depends(get_db)):
    return controller.register(body, db)

@user_routes.post("/login", status_code = status.HTTP_200_OK)
def login_user(body:loginSchema, db:Session = Depends(get_db)):
    return controller.login_user(body, db)

@user_routes.get("/is_auth", status_code = status.HTTP_200_OK, response_model = userResponseSchema)
def is_authentication(request:Request, db:Session = Depends(get_db)):
    return controller.is_authentication(request, db)

