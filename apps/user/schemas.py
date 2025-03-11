from pydantic import BaseModel, Field
from typing import List, Optional
from apps.role.schemas import RoleResponse
from apps.dept.schemas import DeptResponse


class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str
    roles: List[int]
    dept_id: int


class UserResponse(BaseModel):
    username: str
    id: int
    email: str = Field("默认邮箱", alias="email")
    full_name: str = Field("默认昵称", alias="full_name")
    roles: List[RoleResponse] = Field(default_factory=list)
    dept: Optional[DeptResponse] = Field(default=None)
    # hashed_password: str = Field('默认密码', alias="hashed_password")

    class Config:
        from_attributes = True
