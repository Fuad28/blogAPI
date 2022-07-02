from fastapi import APIRouter

blog_router= APIRouter()


blog_router.get('/blog')
def create():
    return 'creating'
