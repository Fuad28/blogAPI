from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from typing import List


from .schemas import UserCreateRequestSchema,  UserCreateResponseSchema
from . import models, hashing
from core.database import engine, get_db

user_router= APIRouter()

models.Base.metadata.create_all(engine)  #creates the tables in the db

@user_router.post('/user', response_model= UserCreateResponseSchema, tags= ["users"])
def create_user(request: UserCreateRequestSchema, db: Session= Depends(get_db)):
    request= dict(request)
    request["password"]= hashing.Hash.bcrypt(request["password"])
    new_user= models.User(**request)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    

@user_router.get('/user', response_model= List[UserCreateResponseSchema], tags= ["users"])
def get_all_users(db: Session = Depends(get_db)):
    blogs = db.query(models.User).all()
    return blogs

@user_router.get('/user/{id}', status_code= status.HTTP_200_OK, response_model= UserCreateResponseSchema, tags= ["users"])
def single_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    return user

@user_router.delete('/user/{id}', status_code= status.HTTP_204_NO_CONTENT, tags= ["users"])
def delete_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    db.delete(user)
    db.commit()
    return {"message": "deleted"}