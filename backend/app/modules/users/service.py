from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.modules.identity.models import User
from app.modules.users.schemas import UserCreateRequest, UserCreateResponse


password_hasher = PasswordHash.recommended()


class EmailAlreadyRegisteredError(Exception):
    """Raised when the email address is already registered."""


def create_user(
    db: Session,
    request: UserCreateRequest,
) -> UserCreateResponse:
    email = str(request.email).strip().lower()

    try:
        # Check for an existing email.
        existing_user = db.scalar(
            select(User).where(User.email == email)
        )

        if existing_user is not None:
            raise EmailAlreadyRegisteredError(
                "An account with this email address already exists."
            )

        # Hash the password before storing it.
        hashed_password = password_hasher.hash(request.password)

        # Create a user record.
        user = User(
            email=email,
            password_hash=hashed_password,
            first_name=request.first_name,
            last_name=request.last_name,
            role="student",
            status="pending",
        )

        db.add(user)
        db.flush()
        db.refresh(user)

        response = UserCreateResponse(
            user_id=user.user_id,
            email=user.email,
            role=user.role,
            status=user.status,
            first_name=user.first_name,
            last_name=user.last_name,
        )

        db.commit()

        return response

    except EmailAlreadyRegisteredError:
        db.rollback()
        raise

    except IntegrityError as exc:
        db.rollback()

        raise EmailAlreadyRegisteredError(
            "The user could not be created because the email may "
            "already be registered or a database constraint failed."
        ) from exc

    except Exception:
        db.rollback()
        raise