from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.curriculum.models import ExamBoard, Subject,SubjectSpecification,SpecificationTier



def get_active_subjects(db: Session) -> list[Subject]:
    statement = (
        select(Subject)
        .where(Subject.is_active.is_(True))
        .order_by(Subject.subject_name)
    )

    return list(db.scalars(statement).all())


def get_active_exam_boards(db: Session) -> list[ExamBoard]:
    statement = (
        select(ExamBoard)
        .where(ExamBoard.is_active.is_(True))
        .order_by(ExamBoard.board_name)
    )

    return list(db.scalars(statement).all())

def get_active_subject_specifications(
    db: Session,
    subject_id: int,
):
    statement = (
        select(SubjectSpecification)
        .where(
            SubjectSpecification.subject_id == subject_id,
            SubjectSpecification.is_active.is_(True),
        )
        .order_by(SubjectSpecification.specification_code)
    )

    specifications = list(db.scalars(statement).all())

    result = []

    for specification in specifications:
        tier_statement = (
            select(SpecificationTier)
            .where(
                SpecificationTier.specification_id
                == specification.specification_id,
                SpecificationTier.is_active.is_(True),
            )
            .order_by(SpecificationTier.specification_tier_id)
        )

        tiers = list(db.scalars(tier_statement).all())

        result.append(
            {
                "specification_id": specification.specification_id,
                "subject_id": specification.subject_id,
                "exam_board_id": specification.exam_board_id,
                "qualification_id": specification.qualification_id,
                "specification_code": specification.specification_code,
                "specification_name": specification.specification_name,
                "specification_version": (
                    specification.specification_version
                ),
                "is_active": specification.is_active,
                "tiers": tiers,
            }
        )

    return result