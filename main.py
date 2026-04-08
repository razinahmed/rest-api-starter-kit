"""
FastAPI application entry point.

Initializes the REST API with CORS, lifespan events, and route registration.
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import init_db
from app.api import auth, users, items

# Import models to ensure they are registered with SQLAlchemy
from app.models import user, item  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage app lifespan: startup and shutdown events.

    Startup: Initialize database
    Shutdown: Clean up resources
    """
    # Startup
    await init_db()
    print("Database initialized")

    yield

    # Shutdown
    print("Application shutting down")


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: Configured application instance
    """
    app = FastAPI(
        title=settings.APP_NAME,
        description="Production-ready REST API with JWT authentication",
        version="1.0.0",
        lifespan=lifespan,
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configure appropriately for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(auth.router, prefix="/api/v1/auth", tags=["authentication"])
    app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
    app.include_router(items.router, prefix="/api/v1/items", tags=["items"])

    @app.get("/health", tags=["health"])
    async def health_check():
        """Health check endpoint."""
        return {"status": "healthy", "app": settings.APP_NAME}

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info",
    )
