from fastapi import FastAPI



from apps.role.urls import role
from apps.user.urls import user



app = FastAPI()

app.include_router(user, prefix="/user", tags=["用户中心"])
app.include_router(role, prefix="/role", tags=["角色信息"])