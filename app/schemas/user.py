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


class UserAuthenticateForm(BaseModel):
    email: EmailStr = Field(max_length=256)
    password: str


class UserResponseSchema(BaseModel):
    username: str = Field(max_length=128)
    email: EmailStr = Field(max_length=256)
    role: Role = Role.USER
    orders: List

    model_config = {
        'from_attributes': True
    }


