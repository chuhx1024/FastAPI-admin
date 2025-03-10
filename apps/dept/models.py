from sqlalchemy import Column, Integer, String
from database.database import Base


class Dept(Base):
    __tablename__ = "depts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), unique=True, index=True)
    desc = Column(String(128), index=True)
    parent_id = Column(Integer, index=True)
