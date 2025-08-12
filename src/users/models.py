from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, validates

from src.database import Base

from .validators import email, phone


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )
    username: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
        nullable=True,
    )
    phone: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
        nullable=True,
    )
    password: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    @validates('email')
    def validate_email(self, field, value):
        if not email(value):
            raise ValueError('Invalid email format')
        return value

    @validates('phone')
    def validate_phone(self, field, value):
        if not phone(value):
            raise ValueError('Invalid phone number format')
        return value
