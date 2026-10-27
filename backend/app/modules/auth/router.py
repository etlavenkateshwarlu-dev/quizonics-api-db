from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.modules.auth.schemas import (
    StudentRegistrationRequest,
    StudentRegistrationResponse,
)
from app.modules.auth.service import (
    EmailAlreadyRegisteredError,
    register_student,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=StudentRegistrationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a student",
    description="Create a student account and its associated profile.",
)
def register_student_endpoint(
    request: StudentRegistrationRequest,
    db: Session = Depends(get_db),
) -> StudentRegistrationResponse:
    """
    Register a new student account.
    """

    try:
        return register_student(
            db=db,
            request=request,
        )

    except EmailAlreadyRegisteredError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc