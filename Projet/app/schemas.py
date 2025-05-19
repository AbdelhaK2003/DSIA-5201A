from pydantic import BaseModel
from typing import Optional, List


class MovieBase(BaseModel):
    title: str
    genre: str
    year: int
    status: str  
    rating: Optional[int] = None
    comment: Optional[str] = None


class MovieCreate(BaseModel):
    title: str
    genre: str
    year: int
    status: str
    rating: Optional[int] = None
    comment: Optional[str] = None

class Movie(MovieCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    movies: List[Movie] = []

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
