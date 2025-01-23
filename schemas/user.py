from pydantic import BaseModel, Field
class UserResponse(BaseModel):
    username: str
    id: int
    email: str = Field('a', alias="email")
    full_name: str = Field('s', alias="full_name")
    hashed_password: str = Field('a', alias="hashed_password")

    class Config:
        orm_mode = True
        from_attributes = True  # 添加这一行