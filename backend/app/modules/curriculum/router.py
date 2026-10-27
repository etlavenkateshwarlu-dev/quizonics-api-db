from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.modules.curriculum import repository
from app.modules.curriculum.schemas import (
    ExamBoardResponse,
    SubjectResponse,
    SubjectSpecificationResponse
)

router = APIRouter(
    prefix="/curriculum",
    tags=["Curriculum"],
)


@router.get(
    "/subjects",
    response_model=list[SubjectResponse],
)
def list_subjects(
    db: Session = Depends(get_db),
):
    return repository.get_active_subjects(db)


@router.get(
    "/exam-boards",
    response_model=list[ExamBoardResponse],
)
def list_exam_boards(
    db: Session = Depends(get_db),
):
    return repository.get_active_exam_boards(db)


@router.get(
    "/subjects/{subject_id}/specifications",
    response_model=list[SubjectSpecificationResponse],
)
def list_subject_specifications(
    subject_id: int,
    db: Session = Depends(get_db),
):
    return repository.get_active_subject_specifications(
        db=db,
        subject_id=subject_id,
    )