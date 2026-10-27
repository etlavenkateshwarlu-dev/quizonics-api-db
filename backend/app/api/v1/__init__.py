from fastapi import APIRouter

from app.modules.curriculum.router import router as curriculum_router
from app.api.v1.endpoints import health

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(curriculum_router)