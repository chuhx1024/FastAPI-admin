from sqlalchemy import Column, Integer, String
from database.database import Base

from sqlalchemy.orm import relationship
from ..user_role_association.models import user_role_association


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    rolename = Column(String(128), unique=True, index=True)

    users = relationship(
        "User", secondary=user_role_association, back_populates="roles"
    )
