from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import JSON
from database.database import Base

from sqlalchemy.orm import relationship
from ..user_role_association.models import user_role_association


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    rolename = Column(String(128), unique=True, index=True)
    permission = Column(JSON)  # 添加 permission 字段，类型为 JSON

    users = relationship(
        "User", secondary=user_role_association, back_populates="roles"
    )
