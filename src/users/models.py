from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, validates

from src.database import Base

from .validators import email


class User(SQLAlchemyBaseUserTable, Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )
    username: Mapped[str] = mapped_column(
        String(length=26),
        unique=True,
        index=True,
        nullable=False,
    )

    @validates('email')
    def validate_email(self, field, value):
        if not email(value):
            raise ValueError('Invalid email format')
        return value
