from fastapi import FastAPI

from sqlalchemy.orm import Session
from database.database import SessionLocal, engine, Base
# from database.model import User

from pydantic import BaseModel

from apps.shop.urls import shop
from apps.user.urls import user

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: str

    class Config:
        orm_mode = True

app.include_router(shop, prefix="/shop", tags=["购物中心"])
app.include_router(user, prefix="/user", tags=["用户中心"])