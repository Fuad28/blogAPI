from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from .schemas import BlogCreateRequestSchema, BlogCreateResponseSchema
from . import models
from core.database import engine, get_db
from authentication.oauth2 import  get_current_user

blog_router= APIRouter()

models.Base.metadata.create_all(engine)  #creates the tables in the db


@blog_router.post('/blog', status_code= status.HTTP_201_CREATED, tags= ["blogs"])
def create(request: BlogCreateRequestSchema, db: Session = Depends(get_db)):
    new_blog= models.Blog(**dict(request))
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@blog_router.get('/blog', response_model= List[BlogCreateResponseSchema], tags= ["blogs"])
def get_all_blogs(db: Session = Depends(get_db), get_current_user: BlogCreateResponseSchema= Depends(get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs

@blog_router.get('/blog/{id}', status_code= status.HTTP_200_OK, response_model= BlogCreateResponseSchema, tags= ["blogs"])
def single_blog(id:int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog

@blog_router.delete('/blog/{id}', status_code= status.HTTP_204_NO_CONTENT, tags= ["blogs"])
def delete(id:int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    db.delete(blog)
    db.commit()
    return {"message": "deleted"}
