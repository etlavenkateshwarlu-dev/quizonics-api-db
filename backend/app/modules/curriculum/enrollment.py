from datetime import datetime

from sqlalchemy import (
BigInteger,
DateTime,
ForeignKey,
ForeignKeyConstraint,
String,
func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class StudentSubject(Base):
"""Model for quizonics.student_subjects."""


__tablename__ = "student_subjects"

__table_args__ = (
    ForeignKeyConstraint(
        ["specification_id", "specification_tier_id"],
        [
            "quizonics.specification_tiers.specification_id",
            "quizonics.specification_tiers.specification_tier_id",
        ],
        name=(
            "student_subjects_specification_id_specification_tier_id_fkey"
        ),
        ondelete="RESTRICT",
    ),
    {"schema": "quizonics"},
)

student_subject_id: Mapped[int] = mapped_column(
    BigInteger,
    primary_key=True,
    autoincrement=True,
)

student_id: Mapped[int] = mapped_column(
    BigInteger,
    ForeignKey(
        "quizonics.student_profiles.student_id",
        name="student_subjects_student_id_fkey",
    ),
    nullable=False,
)

specification_id: Mapped[int] = mapped_column(
    BigInteger,
    ForeignKey(
        "quizonics.subject_specifications.specification_id",
        name="fk_student_subjects_specification",
    ),
    nullable=False,
)

specification_tier_id: Mapped[int] = mapped_column(
    BigInteger,
    nullable=False,
)

target_grade: Mapped[str | None] = mapped_column(
    String,
    nullable=True,
)

enrollment_status: Mapped[str] = mapped_column(
    String,
    nullable=False,
    server_default="ACTIVE",
)

enrolled_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    nullable=False,
    server_default=func.now(),
)

withdrawn_at: Mapped[datetime | None] = mapped_column(
    DateTime(timezone=True),
    nullable=True,
)

created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    nullable=False,
    server_default=func.now(),
)

updated_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    nullable=False,
    server_default=func.now(),
    onupdate=func.now(),
)
