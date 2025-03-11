from fastapi import APIRouter, Body, Depends, HTTPException
from .schemas import LoginRequest, LoginResponse
from schemas.response_models import (
    ResponseModel,
    CustomHTTPException,
    TokenResponseModel,
)
from sqlalchemy.orm import Session
from database.database import get_db
from ..user.models import User
from fastapi.security import OAuth2PasswordRequestForm
from common.passlib_utils import verify_password
from common.jwt_utils import create_access_token

login_router = APIRouter()


@login_router.post("/login")
def login(
    # form_data: LoginRequest = Body(
    #     ...,
    #     title="用户创建信息",
    #     description="包含用户详细信息的请求体",
    #     example={"username": "johndoe", "password": "securepassword123"},
    # ),
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """
    :param username: johndoe
    :param password: securepassword123
    """
    user = db.query(User).filter(User.username == form_data.username).first()
    if user is None:
        # raise CustomHTTPException(status_code=404, message="User not found")
        return ResponseModel(
            code=404,
            data=None,
            msg="用户名不存在",
        )
    if not verify_password(form_data.password, user.hashed_password):
        # raise HTTPException(status_code=401, detail="Incorrect username or password")
        return ResponseModel(
            code=404,
            data=None,
            msg="密码错误",
        )
    access_token = create_access_token(data={"sub": user.username})
    response_data = {"access_token": access_token, "token_type": "bearer"}
    return TokenResponseModel[LoginResponse](
        code=200,
        data=LoginResponse(**response_data),
        access_token=access_token,
        msg="登录成功成功!",
    )
