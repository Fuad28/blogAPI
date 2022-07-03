from typing import List, Optional
from fastapi import FastAPI

from typing import Optional

from blog.main import blog_router, user_router

app= FastAPI()

#register routers
app.include_router(blog_router)
app.include_router(user_router)



@app.get('/')
def index(sort: Optional[str]= None):
    return "heyy"   