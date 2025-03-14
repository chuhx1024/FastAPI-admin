from pydantic import BaseModel
from typing import Optional


class RoleCreate(BaseModel):
    rolename: str


class RoleResponse(BaseModel):
    id: int
    rolename: str
    permission: Optional[str]

    class Config:
        from_attributes = True  # 添加这一行


class MenuEdit(BaseModel):
    permission: str
