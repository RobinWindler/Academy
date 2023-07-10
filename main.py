from typing import Annotated
from fastapi import FastAPI, HTTPException, Depends, Form, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
import jwt

import database as database
from database import get_db, engine

SECRET_KEY = "sage"  # Replace with your own secret key
ALGORITHM = "HS256"

database.Base.metadata.create_all(bind=engine)

app = FastAPI()


# class User(BaseModel):
#     username: str
#     password: str


# def verify_user(username: str, password: str):
#     valid_username = "admin"
#     valid_password = "abcde"

#     if username == valid_username and password == valid_password:
#         return True
#     return False


# def create_jwt_token(username: str):
#     expire = datetime.utcnow() + timedelta(hours=1)
#     payload = {"username": username, "exp": expire}
#     token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
#     return token


@app.get("/all")
async def get_posts(db: Session = Depends(get_db)):
    return {'status': 'success'}
# @app.post("/login")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     username = form_data.username
#     password = form_data.password

#     if not verify_user(username, password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     token = create_jwt_token(username)

#     return {"access_token": token, "token_type": "bearer"}


# @app.post("/register", status_code=status.HTTP_201_CREATED)
# async def register(payload: schemas.CreateUserSchema, request: Request, db: Session = Depends(get_db())):
#     # new_user = model.User(username, password)
#     # db.add(new_user)
#     # db.commit()
#     pass
