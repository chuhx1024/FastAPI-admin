from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True  # 添加这一行
