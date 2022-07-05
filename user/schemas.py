from pydantic import BaseModel
from typing import List


class BlogSchema(BaseModel):
    title: str
    body: str
    user_id: int

    class Config(): 
        orm_mode= True
class UserCreateResponseSchema(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[BlogSchema] = []
    class Config(): 
        orm_mode= True

class UserCreateRequestSchema(BaseModel):
    name: str
    email: str
    password: str
