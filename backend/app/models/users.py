import uuid
from typing import List

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database.base import BaseModel


class Users(BaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    role_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("roles.id"), nullable=True)

    role: Mapped["Roles"] = relationship("Roles", back_populates="users")


class Roles(BaseModel):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    users: Mapped[List["Users"]] = relationship("Users", back_populates="role")
    permissions: Mapped[List["Permissions"]] = relationship(
        "Permissions", back_populates="role"
    )


class Permissions(BaseModel):
    __tablename__ = "permissions"

    name: Mapped[str] = mapped_column(String(100), index=True)
    role_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("roles.id"))

    role: Mapped["Roles"] = relationship("Roles", back_populates="permissions")
