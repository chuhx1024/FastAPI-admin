# models.py
from sqlalchemy import Column, Integer, String
from database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(128), unique=True, index=True)
    email = Column(String(128), unique=True, index=True)
    full_name = Column(String(128), index=True)
    hashed_password = Column(String(128))

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), unique=True, index=True)
    description = Column(String(128))