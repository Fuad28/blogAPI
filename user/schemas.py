from pydantic import BaseModel
from typing import List

from blog.schemas import BlogCreateRequestSchema 

class UserCreateResponseSchema(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[BlogCreateRequestSchema] = []
    class Config(): 
        orm_mode= True

class UserCreateRequestSchema(BaseModel):
    name: str
    email: str
    password: str
