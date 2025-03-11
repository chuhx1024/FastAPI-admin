from pydantic import BaseModel, Field
from typing import Optional, List


class DeptCreate(BaseModel):
    name: str = Field(
        ...,
        description="部门名称",
    )
    desc: str = Field("", description="备注")
    parent_id: int = Field(0, description="父部门ID")


class DeptResponse(BaseModel):
    id: int
    name: str
    desc: str
    parent_id: Optional[int]
    children: List["DeptResponse"] = []

    class Config:
        from_attributes = True  # 添加这一行
