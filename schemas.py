from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel, EmailStr, constr


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr
    # photo: str


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str

    class Config:
        orm_mode = True
    # role: str = 'user'
    # verified: bool = False
