from fastapi import APIRouter, Body, Depends
from .schemas import RoleResponse, RoleCreate, MenuEdit
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


# 给角色添加权限
@role.post(
    "/roles/{role_id}/permission",
    response_model=ResponseModel[RoleResponse],
    summary="给角色添加权限",
)
def add_permission_to_role(
    role_id: int,
    menus: MenuEdit = Body(
        ...,
        title="权限",
        description="包含权限的请求体",
        example={
            "permission": "can_read",
        },
    ),
    db: Session = Depends(get_db),
):
    """
    :param role_id: 角色ID
    :param permission: 权限
    """
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        return ResponseModel(code=404, data={}, msg="角色未找到!")

    print(db_role)
    for key, value in menus.model_dump().items():
        if hasattr(db_role, key):
            setattr(db_role, key, value)

    db.commit()
    db.refresh(db_role)

    return ResponseModel(
        code=200,
        data={
            "rolename": db_role.rolename,
            "id": db_role.id,
            "permission": db_role.permission,
        },
        msg="用户信息更新成功!",
    )


# 根据角色ID获取角色信息
@role.get(
    "/roles/{role_id}",
    response_model=ResponseModel[RoleResponse],
    summary="根据角色ID获取角色信息",
)
def get_role_by_id(
    role_id: int,
    db: Session = Depends(get_db),
):
    """
    :param role_id: 角色ID
    """
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        return ResponseModel(code=404, data={}, msg="角色未找到!")

    return ResponseModel(
        code=200,
        data={
            "rolename": db_role.rolename,
            "id": db_role.id,
            "permission": db_role.permission,
        },
        msg="角色信息获取成功!",
    )
