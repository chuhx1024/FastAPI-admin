from fastapi import APIRouter, Body, Depends
from .schemas import RoleResponse, RoleCreate
from schemas import ResponseModel
from .models import Role
from sqlalchemy.orm import Session
from database.database import get_db

role = APIRouter()


@role.post(
    "/roles",
    response_model=ResponseModel[RoleResponse],
    summary="新建角色",
)
def create_user(
    role: RoleCreate = Body(
        ...,
        title="用户创建信息",
        description="包含用户详细信息的请求体",
        example={
            "rolename": "技术员",
        },
    ),
    db: Session = Depends(get_db),
):
    """
    :param rolename: 角色名称
    """
    role_data = {
        "rolename": role.rolename,
    }
    db_role = Role(**role_data)

    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return ResponseModel(
        code=200,
        data={"rolename": db_role.rolename, "id": db_role.id},
        msg="角色创建成功!",
    )


@role.get(
    "/roles",
    response_model=ResponseModel[list[RoleResponse]],
    summary="获取角色列表",
)
def get_users(
    db: Session = Depends(get_db),
):
    roles = db.query(Role).all()

    # 使用 Pydantic 模型确保数据结构一致
    role_list = [RoleResponse.model_validate(role) for role in roles]

    return ResponseModel(
        code=200,
        data=[role.model_dump() for role in role_list],
        msg="用户角色获取成功!",
    )
