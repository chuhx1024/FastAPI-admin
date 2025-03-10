from pydantic import BaseModel, Field


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
    parent_id: int

    class Config:
        orm_mode = True
