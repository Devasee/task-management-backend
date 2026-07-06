from src.user.dtos import userSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.user.models import userModel
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
def get_password_hash(password):
    return password_hash.hash(password)

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