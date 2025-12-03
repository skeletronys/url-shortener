from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings


# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.project_version,
    debug=settings.debug,
    docs_url="/docs",
    redoc_url="/redoc",
)


# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшені обмежити конкретними доменами
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.project_version
    }


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": f"Welcome to {settings.app_name}",
        "docs": "/docs",
        "health": "/health"
    }


# Event handlers
@app.on_event("startup")
async def startup_event():
    """Run on application startup."""
    print(f"🚀 {settings.app_name} v{settings.project_version} starting...")
    print(f"📝 Debug mode: {settings.debug}")
    print(f"📚 Docs available at: /docs")


@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown."""
    print(f"👋 {settings.app_name} shutting down...")