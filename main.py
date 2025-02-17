from fastapi import FastAPI
from database.database import create_tables

from apps.user.urls import user
from apps.role.urls import role

# 创建数据库表
create_tables()

app = FastAPI()

API_PREFIX = "/api"

app.include_router(user, prefix=f"{API_PREFIX}/user", tags=["用户中心"])
app.include_router(role, prefix=f"{API_PREFIX}/role", tags=["角色信息"])
