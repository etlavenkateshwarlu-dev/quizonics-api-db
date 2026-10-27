from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.curriculum.models import Subject, ExamBoard


def get_active_subjects(db: Session):
    statement = (
        select(Subject)
        .where(Subject.is_active.is_(True))
        .order_by(Subject.subject_name)
    )
    return db.scalars(statement).all()


def get_active_exam_boards(db: Session):
    statement = (
        select(ExamBoard)
        .where(ExamBoard.is_active.is_(True))
        .order_by(ExamBoard.board_name)
    )
    return db.scalars(statement).all()