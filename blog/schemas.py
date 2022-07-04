from pydantic import BaseModel

from user.schemas import UserCreateResponseSchema
class BlogCreateRequestSchema(BaseModel):
    title: str
    body: str
    user_id: int

    class Config(): 
        orm_mode= True   

class BlogCreateResponseSchema(BlogCreateRequestSchema):
    creator: UserCreateResponseSchema
    class Config(): 
        orm_mode= True