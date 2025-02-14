from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str


class UserResponse(BaseModel):
    username: str
    id: int
    email: str = Field("默认邮箱", alias="email")
    full_name: str = Field("默认昵称", alias="full_name")
    # hashed_password: str = Field('默认密码', alias="hashed_password")

    class Config:
        orm_mode = True
        from_attributes = True  # 添加这一行
