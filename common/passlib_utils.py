from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 密码加密
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# 密码校验
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
