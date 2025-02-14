# nodemon --exec python3 ./01.python中的类型声明.py

a: int = 20  # 整数
b: str = "hello"  # 字符串
c: float = 3.14  # 浮点数
d: bool = True  # 布尔值 True 或者 False
e: None = None
f: list = [1, 2, 3]  # 列表
g: dict = {"name": "John", "age": 30}  # 字典
h: tuple = (1, 2, 3)  # 元组
i: set = {1, 2, 3}  # 集合
j: frozenset = frozenset([1, 2, 3])  # 冻结集合
k: bytes = b"Hello"  # 字节串
l: bytearray = bytearray(b"Hello")  # 字节数组
m: memoryview = memoryview(b"Hello")  # 内存视图

print(a, b, c, d, e)
# 数组相关
print("------数组相关---------")
print("f数组的值", f)
print("f数组的值第一项", f[0])
print("f数组的长度", len(f))

for item in f:
    print(item)

index = 0
while index < len(f):
    print(f[index])
    index += 1

if True:
    print("True")

# 字典相关
print("------字典相关---------")
print(g.keys())
print(list(g.keys()))
print(list(g.keys())[0])

# 使用 get 方法
print(g.get("name"))
# 直接使用键
print(g["name"])
# 使用 try-except 块
try:
    address = g["address"]
except KeyError:
    address = "Unknown"
print(address)

# 函数相关
print("------函数相关---------")


def get_name(name: str) -> str:
    return name


def get_age(age: int):
    return age


def get_dict_value(dict: dict):
    return dict["name"]


print(get_dict_value({"name": "小明", "age": 30}))


print(get_name("John"))


print(get_age(40))


def ccc(a: int, b: int) -> int:
    return a + b


print(ccc(a=1, b=2))
print(ccc(33, 99))

dict0 = {"a": 124, "b": 1}
print({**dict0})
print(ccc(**dict0))

# -元组相关
print("------元组相关---------")
print(h)
print(h[0])
h0 = (123,)  # 元组中只有一个元素的时候，需要加逗号
print(h0)
h1 = (  # 元组中可以包含多个元素，可以是任意类型
    "我是元组的第一个值",
    {"name": "John", "age": 30},
    "字符串",
    True,
    (123, 456),
    [1, 2, 3],
)
print(h1)
print(h1[0])
print(h1[4])
print(h1[4][0])
h1[5].append(4)
print(h1)
key = (12, 99)
print(key)
key0 = [12, 99]
tupleDict = {
    ("name",): "John",
    (10, 20): 30,
    key: "我的键值是一个元组",
    "phone": key,
}
key = (12, 99, 123)
print(tupleDict, 11111)
print(tupleDict[("name",)])
# print(tupleDict[key])
print(tupleDict.get((10, 20)))

# 集合相关
print("------集合相关---------")
print(i)
i.add(4)
print(i)
i.remove(1)
print(i)

# 类相关
print("------类相关---------")


class User:
    # 类属性
    species = "Human"

    # 初始化方法（构造函数）
    def __init__(
        self,
        email: str,
        full_name: str,
        hashed_password: str,
        username: str = "123",
    ):
        # 实例属性
        self.username = username
        self.email = email
        self.full_name = full_name
        self.hashed_password = hashed_password

    # 实例方法
    def greet(self) -> str:
        return f"Hello, my name is {self.full_name} and my username is {self.username}."

    # 类方法
    @classmethod
    def create_anonymous(cls) -> "User":
        return cls(
            username="anonymous",
            email="anonymous@example.com",
            full_name="Anonymous",
            hashed_password="",
        )

    # 静态方法
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18


# 创建类的实例
user1 = User(
    username="john_doe",
    email="john@example.com",
    full_name="John Doe",
    hashed_password="hashed_password",
)

dict00 = {
    # "username": "john_doe222",
    "email": "john@example.com",
    "full_name": "John Doe",
    "hashed_password": "hashed_password",
}
user2 = User(**dict00)

# 访问类
print(User.create_anonymous())
print(User.is_adult(33))  # 输出: True

# 访问实例属性
print(user1.username)  # 输出: john_doe
print(user1.is_adult(33))  # 输出: True
print(user1.create_anonymous())

print(user2.username)  # 输出: 123
