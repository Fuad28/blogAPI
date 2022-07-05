from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session


from .schemas import  LoginRequestSchema
from fastapi.security import OAuth2PasswordRequestForm


from core.database import get_db
from core.hashing import Hash
from user.models import User
from .token import create_access_token


auth_router = APIRouter(prefix= "/auth", tags= ["Authentication"])

@auth_router.post('/login')
def login(request: OAuth2PasswordRequestForm= Depends(), db: Session = Depends(get_db)): 
    user= db.query(User).filter(User.email== request.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")


    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
 
