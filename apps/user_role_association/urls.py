from fastapi import APIRouter, Body, Depends, Path
from schemas import ResponseModel
from sqlalchemy.orm import Session
from database.database import get_db
from .schemas import UserAddRoleCreate
from .models import user_role_association
from ..user.models import User
from ..role.models import Role

user_role_router = APIRouter()


@user_role_router.post(
    "/userAddRole/",
    summary="用户添加角色",
)
def addRole(
    ids: UserAddRoleCreate = Body(
        ...,
        title="用户添加角色",
        description="包含详细信息的请求体",
        example={"user_id": 1, "role_ids": [1, 2]},
    ),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.id == ids.user_id).first()
    if not user:
        return ResponseModel(code=404, data={}, msg="用户未找到!")

    roles = db.query(Role).filter(Role.id.in_(ids.role_ids)).all()
    if len(roles) != len(ids.role_ids):
        return ResponseModel(code=404, data={}, msg="部分角色未找到!")

    user.roles.extend(roles)
    db.commit()
    db.refresh(user)

    return ResponseModel(
        code=200,
        data={"user_id": user.id, "roles": [role.rolename for role in user.roles]},
        msg="角色分配成功!",
    )


@user_role_router.get(
    "/user/{user_id}/roles/",
    summary="根据用户ID查询角色",
)
def get_user_roles(
    user_id: int = Path(..., title="用户ID", description="用户ID"),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return ResponseModel(code=404, data={}, msg="用户未找到!")

    roles = [{"rolename": role.rolename, "id": role.id} for role in user.roles]

    return ResponseModel(
        code=200,
        data={"user_id": user.id, "roles": roles},
        msg="查询成功!",
    )
