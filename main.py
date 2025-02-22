from fastapi import FastAPI
from database.database import create_tables

from apps.user.urls import user
from apps.role.urls import role
from apps.user_role_association.urls import user_role_router
from apps.login.urls import login_router

# 创建数据库表
create_tables()

app = FastAPI()

API_PREFIX = "/api"

app.include_router(user, prefix=f"{API_PREFIX}/user", tags=["用户中心"])
app.include_router(role, prefix=f"{API_PREFIX}/role", tags=["角色信息"])
app.include_router(
    user_role_router, prefix=f"{API_PREFIX}/userAddRole", tags=["用户添加角色"]
)
app.include_router(login_router, prefix=f"{API_PREFIX}", tags=["登录信息"])
