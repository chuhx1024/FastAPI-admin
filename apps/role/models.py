from sqlalchemy import Column, Integer, String
from database.database import Base
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    rolename = Column(String(128), unique=True, index=True)
