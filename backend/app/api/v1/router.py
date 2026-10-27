from fastapi import APIRouter

from app.api.v1.endpoints import health
from app.modules.auth.router import router as auth_router
from app.modules.curriculum.router import router as curriculum_router
from app.modules.users.router import router as users_router
api_router = APIRouter()

# Authentication APIs
api_router.include_router(auth_router)

# Curriculum APIs
api_router.include_router(curriculum_router)

# Health APIs
api_router.include_router(health.router)

api_router.include_router(users_router)