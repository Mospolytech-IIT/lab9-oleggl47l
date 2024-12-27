"""schemas"""
from pydantic import BaseModel

class UserCreate(BaseModel):
    """UserCreate"""
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    """UserUpdate"""
    username: str
    email: str
    password: str

class PostCreate(BaseModel):
    """PostCreate"""
    title: str
    content: str
    user_id: int

class PostUpdate(BaseModel):
    """PostUpdate"""
    title: str
    content: str

# Схемы для вывода данных
class UserOut(BaseModel):
    """UserOut"""
    id: int
    username: str
    email: str

class PostOut(BaseModel):
    """PostOut"""
    id: int
    title: str
    content: str
    user_id: int
