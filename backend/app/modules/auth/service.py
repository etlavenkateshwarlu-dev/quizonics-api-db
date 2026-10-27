from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from pwdlib import PasswordHash

from app.modules.identity.models import User
from app.modules.auth.schemas import (
    StudentRegistrationRequest,
    StudentRegistrationResponse,
)
from app.modules.identity import repository


password_hasher = PasswordHash.recommended()


class EmailAlreadyRegisteredError(Exception):
    """Raised when an email address is already registered."""


def register_student(
    db: Session,
    request: StudentRegistrationRequest,
) -> StudentRegistrationResponse:
    """
    Register a user in quizonics.users only.
    Passwords are hashed before storage.
    """

    email = str(request.email).strip().lower()

    try:
        # Check whether the email already exists.
        existing_user = repository.get_user_by_email(
            db=db,
            email=email,
        )

        if existing_user is not None:
            raise EmailAlreadyRegisteredError(
                "An account with this email address already exists."
            )

        # Hash the password.
        password_hash = password_hasher.hash(request.password)

        # Create the user record.
        user = User(
            email=email,
            password_hash=password_hash,
            first_name=request.first_name,
            last_name=request.last_name,
            role="student",
            status="pending",
        )

        repository.create_user(db=db, user=user)

        # Insert into the users table.
        db.flush()
        db.refresh(user)

        # Build the response without creating a student profile.
        response = StudentRegistrationResponse(
            user_id=user.user_id,
            student_id=None,
            email=user.email,
            role=user.role,
            status=user.status,
            first_name=user.first_name,
            last_name=user.last_name,
            school_year=request.school_year,
            school_name=request.school_name,
        )

        # Commit the user record.
        db.commit()

        return response

    except EmailAlreadyRegisteredError:
        db.rollback()
        raise

    except IntegrityError:
        db.rollback()

        existing_user = repository.get_user_by_email(
            db=db,
            email=email,
        )

        if existing_user is not None:
            raise EmailAlreadyRegisteredError(
                "An account with this email address already exists."
            )

        raise

    except Exception:
        db.rollback()
        raise