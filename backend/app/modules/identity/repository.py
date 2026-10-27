from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.identity.models import User, Role


def get_user_by_email(db: Session, email: str) -> User | None:
    """Find a user by email."""
    statement = select(User).where(User.email == email)
    return db.scalars(statement).first()


def get_role_by_code(db: Session, role_code: str) -> Role | None:
    """Find a role by its role code."""
    statement = select(Role).where(Role.role_code == role_code)
    return db.scalars(statement).first()


def create_user(db: Session, user: User) -> User:
    """Add a user to the database session."""
    db.add(user)
    return user