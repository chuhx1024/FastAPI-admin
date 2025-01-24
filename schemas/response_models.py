from pydantic import BaseModel, Field
from typing import  Optional, TypeVar, Generic



# 定义一个类型变量
T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
    code: int = Field(200, alias="code", description="状态码")
    data: T = Field(None, alias="data", description="返回数据")
    msg: Optional[str] = Field("获取用户信息成功", alias="msg", description="状态信息")

    class Config:
        orm_mode = True

