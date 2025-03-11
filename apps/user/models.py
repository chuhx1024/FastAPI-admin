from sqlalchemy import Column, Integer, String, ForeignKey
from database.database import Base

from sqlalchemy.orm import relationship
from ..user_role_association.models import user_role_association


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(128), unique=True, index=True)
    email = Column(String(128), index=True)
    full_name = Column(String(128), index=True)
    hashed_password = Column(String(128))
    dept_id = Column(Integer, ForeignKey("depts.id"))

    roles = relationship(
        "Role", secondary=user_role_association, back_populates="users"
    )
    dept = relationship("Dept", back_populates="users")
