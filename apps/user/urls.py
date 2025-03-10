from fastapi import APIRouter, Depends, HTTPException, Body, Path

from sqlalchemy.orm import Session
from database.database import get_db
from schemas import ResponseModel
from .models import User
from .schemas import UserCreate, UserResponse
from common.passlib_utils import hash_password
from common.jwt_utils import get_current_user, oauth2_scheme


user = APIRouter()


@user.post(
    "/users/",
    response_model=ResponseModel[UserResponse],
    summary="新建用户",
)
def create_user(
    user: UserCreate = Body(
        ...,
        title="用户创建信息",
        description="包含用户详细信息的请求体",
        example={
            "username": "johndoe",
            "email": "johndoe@example.com",
            "full_name": "John Doe",
            "password": "securepassword123",
        },
    ),
    db: Session = Depends(get_db),
):
    """
    :param username: 用户名
    :param email: 邮箱
    """
    user_data = {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": hash_password(
            user.password
        ),  # In a real application, hash the password
    }

    db_user = User(**user_data)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return ResponseModel(
        code=200,
        data={"username": db_user.username, "id": db_user.id, "email": db_user.email},
        msg="用户创建成功!",
    )


@user.get(
    "/users/{user_id}",
    response_model=ResponseModel[UserResponse],
    summary="通过id获取用户信息",
)
def get_user(
    user_id: int = Path(..., title="用户ID", description="用户的唯一标识,gt=0"),
    db: Session = Depends(get_db),
):
    """
    这里也可以写一些文档注释，用于描述该路由的用途、参数和返回值
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    roles = db_user.roles
    return ResponseModel(
        code=200,
        data=dict(
            username=db_user.username,
            id=db_user.id,
            email=db_user.email,
            full_name=db_user.full_name,
            roles=[{"id": role.id, "rolename": role.rolename} for role in roles],
        ),
        msg="用户获取成功!",
    )


@user.get(
    "/users/",
    response_model=ResponseModel[list[UserResponse]],
    summary="获取用户列表",
    dependencies=[Depends(oauth2_scheme)],
)
def get_users(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    users = db.query(User).all()
    # user_list = [
    #     dict(
    #         username=user.username,
    #         id=user.id
    #     )
    #     for user in users
    # ]
    # user_list = [{"username": user.username, "id": user.id} for user in users]

    # user_list = []
    # for user in users:
    #     user_list.append({
    #         "username": user.username,
    #         "id": user.id
    #     })

    # return ResponseModel(
    #     code=200,
    #     data=user_list,
    #     msg="用户列表获取成功!",
    # )

    # 使用 Pydantic 模型确保数据结构一致
    user_list = [UserResponse.model_validate(user) for user in users]
    print(user_list)

    return ResponseModel(
        code=200,
        data=[user.model_dump() for user in user_list],
        msg="用户列表获取成功!",
    )


@user.put(
    "/users/{user_id}",
    response_model=ResponseModel,
    summary="更新用户信息",
    description="通过用户ID更新用户的用户名、电子邮件和全名。",
)
def update_user(user_id: int, user_update: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    print(user_update.dict())
    for key, value in user_update.dict().items():
        if hasattr(db_user, key):
            setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return ResponseModel(
        code=200,
        data=dict(
            username=db_user.username,
            id=db_user.id,
            email=db_user.email,
            full_name=db_user.full_name,
        ),
        msg="用户信息更新成功!",
    )
