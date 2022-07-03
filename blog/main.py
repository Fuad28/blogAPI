from os import sync
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response

from sqlalchemy.orm import Session

from .schemas import BlogCreateRequestSchema, BlogCreateResponseSchema
from .database import engine, get_db
from . import models

blog_router= APIRouter()

models.Base.metadata.create_all(engine)  #creates the tables in the db


@blog_router.post('/blog', status_code= status.HTTP_201_CREATED)
def create(request: BlogCreateRequestSchema, db: Session = Depends(get_db)):
    new_blog= models.Blog(title= request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@blog_router.get('/blog', response_model= List[BlogCreateResponseSchema])
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@blog_router.get('/blog/{id}', status_code= status.HTTP_200_OK, response_model= BlogCreateResponseSchema)
def single_blog(id:int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog

@blog_router.delete('/blog/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete(id:int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    db.delete(blog)
    db.commit()
    return {"message": "deleted"}


############ USERS ##################