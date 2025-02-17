from pydantic import BaseModel, Field
from typing import List


class UserAddRoleCreate(BaseModel):
    user_id: int = Field(..., title="用户ID", description="用户ID")
    role_ids: List[int] = Field(..., title="角色ID列表", description="角色ID列表")
