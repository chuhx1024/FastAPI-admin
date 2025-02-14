from fastapi import APIRouter, Depends

from fastapi import APIRouter, Body
from sqlalchemy.orm import Session
from database.database import get_db
from schemas import ResponseModel
from .models import User
from .schemas import UserCreate, UserResponse


user = APIRouter()


@user.post(
    "/users/",
    response_model=ResponseModel[UserResponse],
    summary="新建用户",
)
def create_user(
    user: UserCreate = Body(
        ...,
        title="用户创建信息",
        description="包含用户详细信息的请求体",
        example={
            "username": "johndoe",
            "email": "johndoe@example.com",
            "full_name": "John Doe",
            "password": "securepassword123",
        },
    ),
    db: Session = Depends(get_db),
):
    """
    :param username: 用户名
    :param email: 邮箱
    """
    user_data = {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": user.password,  # In a real application, hash the password
    }

    db_user = User(**user_data)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return ResponseModel(
        code=200,
        data={"username": db_user.username, "id": db_user.id, "email": db_user.email},
        msg="用户创建成功!",
    )
