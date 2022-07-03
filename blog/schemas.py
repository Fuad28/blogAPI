from pydantic import BaseModel

class BlogCreateRequestSchema(BaseModel):
    title: str
    body: str

     

class BlogCreateResponseSchema(BlogCreateRequestSchema):
    class Config(): 
        orm_mode= True


class UserCreateRequestSchema(BaseModel):
    name: str
    email: str
    password: str

class UserCreateResponseSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str
