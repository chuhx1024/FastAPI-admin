from pydantic import BaseModel, Field
from typing import List, Optional
from apps.role.schemas import RoleResponse
from apps.dept.schemas import DeptResponse


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True  # 添加这一行


class UserInfoResponse(BaseModel):
    username: str
    id: int
    email: str = Field("默认邮箱", alias="email")
    full_name: str = Field("默认昵称", alias="full_name")
    roles: List[RoleResponse] = Field(default_factory=list)
    dept: Optional[DeptResponse] = Field(default=None)
