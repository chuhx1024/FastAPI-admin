from sqlalchemy import Column, Integer, String
from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(128), unique=True, index=True)
    email = Column(String(128), index=True)
    full_name = Column(String(128), index=True)
    hashed_password = Column(String(128))
