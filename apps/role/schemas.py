from pydantic import BaseModel, Field


class RoleCreate(BaseModel):
    rolename: str


class RoleResponse(BaseModel):
    id: int
    rolename: str

    class Config:
        from_attributes = True  # 添加这一行
