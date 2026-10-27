from sqlalchemy import (
    BigInteger,
    Boolean,
    String,
    Text,
    Date,
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Subject(Base):
    __tablename__ = "subjects"
    __table_args__ = {"schema": "quizonics"}

    subject_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True
    )
    subject_code: Mapped[str] = mapped_column(
        String(40), nullable=False
    )
    subject_name: Mapped[str] = mapped_column(
        String(150), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False
    )


class ExamBoard(Base):
    __tablename__ = "exam_boards"
    __table_args__ = {"schema": "quizonics"}

    exam_board_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True
    )
    board_code: Mapped[str] = mapped_column(
        String(30), nullable=False
    )
    board_name: Mapped[str] = mapped_column(
        String(150), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False
    )


class SubjectSpecification(Base):
    __tablename__ = "subject_specifications"
    __table_args__ = {"schema": "quizonics"}

    specification_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True
    )
    subject_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("quizonics.subjects.subject_id"),
        nullable=False,
    )
    exam_board_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("quizonics.exam_boards.exam_board_id"),
        nullable=False,
    )
    qualification_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("quizonics.qualifications.qualification_id"),
        nullable=False,
    )
    specification_code: Mapped[str] = mapped_column(
        String, nullable=False
    )
    specification_name: Mapped[str] = mapped_column(
        String, nullable=False
    )
    specification_version: Mapped[str | None] = mapped_column(
        String, nullable=True
    )
    effective_from: Mapped[Date | None] = mapped_column(
        Date, nullable=True
    )
    effective_to: Mapped[Date | None] = mapped_column(
        Date, nullable=True
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )


class SpecificationTier(Base):
    __tablename__ = "specification_tiers"
    __table_args__ = {"schema": "quizonics"}

    specification_tier_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True
    )
    specification_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(
            "quizonics.subject_specifications.specification_id"
        ),
        nullable=False,
    )
    tier_code: Mapped[str] = mapped_column(
        String, nullable=False
    )
    tier_name: Mapped[str] = mapped_column(
        String, nullable=False
    )
    description: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default="true"
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), nullable=False,
        server_default=func.current_timestamp(),
    )