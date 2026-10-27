from datetime import datetime
from uuid import UUID

#from sqlalchemy import String, Text, TIMESTAMP, text,BigInteger,Boolean
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    Date,
    ForeignKey,
    String,
    Text,
    TIMESTAMP,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "quizonics"}

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )

    # Python attribute password_hash maps to database column password.
    password_hash: Mapped[str] = mapped_column(
        "password",
        Text,
        nullable=False,
    )

    role: Mapped[str] = mapped_column(
        String,
        nullable=False,
        server_default=text("'student'"),
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
        server_default=text("'pending'"),
    )

    email_verified_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("now()"),
    )

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("now()"),
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

class Role(Base):
    __tablename__ = "roles"
    __table_args__ = {"schema": "quizonics"}

    role_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
    )

    role_code: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )

    role_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

class StudentProfile(Base):
    __tablename__ = "student_profiles"
    __table_args__ = {"schema": "quizonics"}

    student_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
    )

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(
            "quizonics.users.user_id",
            ondelete="CASCADE",
        ),
        nullable=False,
        unique=True,
    )

    date_of_birth: Mapped[datetime | None] = mapped_column(
        Date,
        nullable=True,
    )

    academic_year: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    school_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    profile_status: Mapped[str] = mapped_column(
        String,
        nullable=False,
        server_default=text("'ACTIVE'"),
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

class UserRole(Base):
    __tablename__ = "user_roles"
    __table_args__ = {"schema": "quizonics"}

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(
            "quizonics.users.user_id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    role_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(
            "quizonics.roles.role_id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    assigned_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )