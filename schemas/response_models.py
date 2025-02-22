from pydantic import BaseModel, Field
from typing import Optional, TypeVar, Generic, Any
from fastapi import HTTPException


# 定义一个类型变量
T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    code: int = Field(200, alias="code", description="状态码")
    data: T
    msg: Optional[str] = Field("获取用户信息成功", alias="msg", description="状态信息")

    class Config:
        from_attributes = True


# 必须在 返回token 的接口 返回 access_token FastApi的文档登录才能找到 token  要不就是 undifined
class TokenResponseModel(BaseModel, Generic[T]):
    code: int = Field(200, alias="code", description="状态码")
    data: T
    access_token: str
    msg: Optional[str] = Field("获取用户信息成功", alias="msg", description="状态信息")

    class Config:
        from_attributes = True


class CustomErrorResponse(BaseModel):
    code: int
    message: str
    detail: Any = None


class CustomHTTPException(HTTPException):
    def __init__(
        self,
        status_code: int,
        message: str,
    ):
        super().__init__(
            status_code=status_code,
            detail=ResponseModel(code=status_code, data={}, msg=message).dict(),
        )
