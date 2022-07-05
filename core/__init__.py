from typing import List, Optional
from fastapi import FastAPI

from typing import Optional

from blog.main import blog_router
from user.main import user_router
from authentication.main import auth_router


app= FastAPI()

#register routers
app.include_router(blog_router)
app.include_router(user_router)
app.include_router(auth_router)



@app.get('/')
def index(sort: Optional[str]= None):
    return "heyy"   