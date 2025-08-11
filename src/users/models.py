from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import validates

from src.database import Base

from .validators import email, phone


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    phone = Column(String, unique=True, index=True, nullable=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

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
