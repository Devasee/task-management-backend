from src.user.dtos import userSchema, loginSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.user.models import userModel
from pwdlib import PasswordHash
from src.utils.settings import settings
from datetime import datetime, timedelta
import jwt

password_hash = PasswordHash.recommended()
#make password to the hash password
def get_password_hash(password):
    return password_hash.hash(password)

#helps to match that the user enteres password matches the hash password or not 
def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def register(body:userSchema, db:Session):
    is_user = db.query(userModel).filter(userModel.username == body.username).first()
    if(is_user):
        raise HTTPException(404, detail = "Username already exists")
    
    is_user = db.query(userModel).filter(userModel.email == body.email).first()
    if(is_user):
        raise HTTPException(404, detail = "Email already exists")
    
    hashed_password = get_password_hash(body.password)

    new_user = userModel(
        name = body.name,
        username = body.username,
        hashed_password = hashed_password,
        email = body.email,
        mobile = body.mobile
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(body: loginSchema, db:Session):
    user = db.query(userModel).filter(userModel.username == body.username).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "User does not exist")
    
    if not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "You entered wrong password")
    
    exp_time = datetime.now() + timedelta(minutes =settings.EXP_TIME)
    token = jwt.encode({"_id" : user.id, "username" : body.username, "exp" : exp_time}, settings.SECRET_KEY, settings.ALGORITHM) #{} -> payload, store unique values(username, id, email), can be multiple(even if one pass the token will be generated),  at what basis you want to generate the token
                             #secret key -> helps to encode or decode the token
                             #algorithm -> which algo will be used to encode or decode the code 
                             ## exp -> it expire the token after some time aslo it the main reason that the token keeps changing after some time, so that the user can not use the same token again and again, it will expire after some time

    return {"token": token}