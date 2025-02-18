# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 替换为你的 MariaDB 用户名、密码、主机和数据库名称

# mysql 配置
MYSQL_USERNAME: str = "root"
MYSQL_PASSWORD: str = "admin12345"
MYSQL_HOST = "127.0.0.1:3306"
MYSQL_DATABASE: str = "FastAdmin"

# mysql地址
SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@"
    f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True  # 设置为 True 以查看 SQL 查询日志，调试时使用
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# 创建数据库表
def create_tables():
    Base.metadata.create_all(bind=engine)
