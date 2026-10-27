from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter(tags=["Health"])


@router.get("/")
def root():
    return {
        "success": True,
        "message": "Welcome to Quizonics API",
        "version": "1.0.0",
    }


@router.get("/health")
def health_check():
    return {
        "success": True,
        "status": "healthy",
        "service": "quizonics-backend",
    }


@router.get("/database")
def database_health(db: Session = Depends(get_db)):
    try:
        result = db.execute(
            text("""
                SELECT
                    current_database() AS database_name,
                    current_schema() AS current_schema
            """)
        ).mappings().one()

        return {
            "success": True,
            "database_status": "connected",
            "database_name": result["database_name"],
            "current_schema": result["current_schema"],
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database connection is unavailable",
        )