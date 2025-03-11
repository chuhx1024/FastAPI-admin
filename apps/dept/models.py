from sqlalchemy import Column, Integer, String
from database.database import Base
from sqlalchemy.orm import relationship


class Dept(Base):
    __tablename__ = "depts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), unique=True, index=True)
    desc = Column(String(128), index=True)
    parent_id = Column(Integer, index=True)

    users = relationship("User", back_populates="dept")  # 添加 users 关系
