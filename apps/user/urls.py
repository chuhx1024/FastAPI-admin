from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from database.database import get_db
from schemas import ResponseModel
from .models import User
from .schemas import UserCreate, UserResponse

user = APIRouter()

@user.post("/users/", response_model=ResponseModel[UserResponse], summary="新建用户",)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=user.password  # In a real application, hash the password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return ResponseModel(
        # data=dict(
        #     username=db_user.username, 
        #     id=db_user.id,
        #     email=db_user.email
        # ),
        data={
            "username":db_user.username, 
            "id":db_user.id,
            "email":db_user.email
        },
        msg="用户创建成功!"
    )

@user.get("/users/{user_id}", response_model=ResponseModel[UserResponse], summary="通过id获取用户信息",)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return ResponseModel(
        data=dict(
            username=db_user.username, 
            id=db_user.id,
            email=db_user.email
        ),
    )
    # return db_user

@user.get("/users/", response_model=ResponseModel[list[UserResponse]], summary="获取用户列表",)
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    # user_list = [
    #     dict(
    #         username=user.username, 
    #         id=user.id
    #     )
    #     for user in users
    # ]
    user_list = [{"username": user.username,"id": user.id} for user in users]

    # user_list = []
    # for user in users:
    #     user_list.append({
    #         "username": user.username,  
    #         "id": user.id
    #     })

    return ResponseModel( data=user_list )


@user.put("/users/{user_id}", response_model=ResponseModel, summary="更新用户信息", description="通过用户ID更新用户的用户名、电子邮件和全名。")
def update_user(user_id: int, user_update: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update user fields
    db_user.username = user_update.username
    db_user.email = user_update.email
    db_user.full_name = user_update.full_name
    
    db.commit()
    db.refresh(db_user)
    
    return ResponseModel(
        data=dict(
            username=db_user.username, 
            id=db_user.id,
            email=db_user.email,
            full_name=db_user.full_name
        ),
        msg="用户信息更新成功!"
    )