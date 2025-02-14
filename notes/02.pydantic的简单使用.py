from pydantic import BaseModel, ValidationError


class UserCreate(BaseModel):
    email: str
    full_name: str
    password: str
    username: str = "我是默认值"


def user(stu: UserCreate):
    print(stu.email)


def userTodicts(stu: UserCreate):
    data = stu.model_dump(exclude={"password"})  # 转换为字典 默认排除password字段
    print(data)


def userToSelf(stu: UserCreate):
    data = stu
    print(data)


user_data = {
    "email": "123@qq.com",
    "full_name": "张三",
    "password": "123456",
    # "username": "zhangsan",
}
print(UserCreate(**user_data))
if __name__ == "__main__":
    print("-------------")
user(
    UserCreate(
        username="zhangsan", email="1266663@qq.com", password="123456", full_name="张三"
    )
)

try:
    user(UserCreate(**user_data))
except ValidationError as e:
    print(e.errors(), 12399999)

# user("12", "22", "33", "44")
user(UserCreate(**user_data))
userTodicts(UserCreate(**user_data))
userToSelf(UserCreate(**user_data))
