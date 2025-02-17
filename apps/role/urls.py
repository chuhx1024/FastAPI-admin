from fastapi import APIRouter, Body, Depends
from .schemas import RoleResponse, RoleCreate
from schemas import ResponseModel
from .models import Role
from sqlalchemy.orm import Session
from database.database import get_db

role = APIRouter()


@role.get("/roles/")
def shop_root():
    return {"Hello": "World"}


@role.get("/bad")
def shop_bad():
    return {"shop": "bad"}


@role.post(
    "/roles/",
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
