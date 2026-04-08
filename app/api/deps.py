"""
API dependencies.

Provides dependency functions for routes, including:
- Database session
- Current authenticated user
"""
from typing import AsyncGenerator

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_db as get_database
from app.core.security import verify_token
from app.models.user import User


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Get database session dependency.

    Yields:
        AsyncSession: Database session

    Example:
        @app.get("/users")
        async def get_users(db: AsyncSession = Depends(get_db)):
            ...
    """
    async for session in get_database():
        yield session


async def get_current_user(
    token: str = Depends(get_token),
    db: AsyncSession = Depends(get_db),
) -> User:
    """
    Get the current authenticated user from JWT token.

    Args:
        token: JWT token from Authorization header
        db: Database session

    Returns:
        User: The authenticated user

    Raises:
        HTTPException: If token is invalid or user not found
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user_id = verify_token(token)
    if user_id is None:
        raise credentials_exception

    # Fetch user from database
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()

    if user is None or not user.is_active:
        raise credentials_exception

    return user


def get_token(authorization: str = None) -> str:
    """
    Extract JWT token from Authorization header.

    Args:
        authorization: Authorization header value

    Returns:
        str: JWT token

    Raises:
        HTTPException: If token is missing or malformed
    """
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authorization header",
            headers={"WWW-Authenticate": "Bearer"},
        )

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return token
