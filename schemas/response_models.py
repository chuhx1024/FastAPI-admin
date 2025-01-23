from pydantic import BaseModel, Field
from typing import  Optional, Union

from schemas.user import UserResponse 

class ResponseModel(BaseModel):
    code: int = Field(200, alias="code", description="状态码")
    data: Union[UserResponse, list[UserResponse], None] = Field(None, alias="data", description="返回数据")
    msg: Optional[str] = Field("获取用户信息成功", alias="msg", description="状态信息")

    class Config:
        orm_mode = True

