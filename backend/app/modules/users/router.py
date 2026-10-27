from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.modules.users.schemas import UserCreateRequest, UserCreateResponse
from app.modules.users.service import (
    EmailAlreadyRegisteredError,
    create_user,
)


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "",
    response_model=UserCreateResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a user",
    description="Insert a user into the existing quizonics.users table.",
)
def create_user_endpoint(
    request: UserCreateRequest,
    db: Session = Depends(get_db),
) -> UserCreateResponse:
    try:
        return create_user(db=db, request=request)

    except EmailAlreadyRegisteredError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc  