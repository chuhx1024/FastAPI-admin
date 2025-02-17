from sqlalchemy import Column, Integer, String, Table, ForeignKey
from database.database import Base

user_role_association = Table(
    "user_role_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("role_id", Integer, ForeignKey("roles.id")),
)
