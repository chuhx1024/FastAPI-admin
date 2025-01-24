# models.py
from sqlalchemy import Column, Integer, String
from database.database import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), unique=True, index=True)
    description = Column(String(128))