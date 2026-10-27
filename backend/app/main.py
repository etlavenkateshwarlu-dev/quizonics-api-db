from fastapi import FastAPI
from app.api.v1.router import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Quizonics API",
    description="""
    ## Quizonics Backend API

    Backend services for the Quizonics education platform.

    ### Features
    - Student registration and authentication
    - Student profiles
    - Subjects and exam boards
    - Question bank
    - Examinations
    - Results and performance analytics

    **Architecture:** Modern Modular Monolith

    **Backend:** Python + FastAPI

    **Database:** PostgreSQL
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "Accept"],
)
app.include_router(
    api_router,
    prefix="/api/v1",
)

@app.get("/", tags=["Health"])
def root():
    return {
        "success": True,
        "message": "Welcome to Quizonics API",
        "version": "1.0.0",
    }


@app.get("/api/v1/health", tags=["Health"])
def health_check():
    return {
        "success": True,
        "status": "healthy",
        "service": "quizonics-backend",
    }