from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    username: Optional[str] = None
    password_hash: Optional[str] = None


class UserLogin(BaseModel):
    username: str
    password: str


class UserUpdatePassword(BaseModel):
    password_hash: str

