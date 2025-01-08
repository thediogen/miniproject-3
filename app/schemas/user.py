from typing import List, Annotated
from enum import Enum
import uuid

from pydantic import BaseModel, EmailStr, Field


class Role(str, Enum):
    ADMIN = 'admin'
    USER = 'user'
    SELLER = 'seller'


class UserSchema(BaseModel):
    username: str = Field(max_length=128)
    email: EmailStr = Field(max_length=256)
    password: str
    role: Role = Role.USER

class UserResponseSchema(UserSchema):
    id: uuid.UUID
    token: str
    orders: List

class UserAuthenticateForm(UserSchema):
    ...

class UserAuthorizeForm(BaseModel):
    email: EmailStr = Field(max_length=256)
    password: str
