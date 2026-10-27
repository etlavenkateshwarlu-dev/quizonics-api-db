from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    Provide a SQLAlchemy database session for a FastAPI request.

    The session is closed when the request finishes.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()