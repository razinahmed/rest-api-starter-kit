"""
User management routes.

Provides CRUD endpoints for user operations.
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate
from app.core.security import hash_password

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Get current authenticated user information.

    Args:
        current_user: Current authenticated user

    Returns:
        User: Current user information
    """
    return current_user


@router.put("/me", response_model=UserResponse)
async def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> User:
    """
    Update current user's information.

    Args:
        user_update: User update data
        current_user: Current authenticated user
        db: Database session

    Returns:
        User: Updated user

    Raises:
        HTTPException: If user not found or error during update
    """
    if user_update.full_name is not None:
        current_user.full_name = user_update.full_name

    if user_update.password is not None:
        current_user.hashed_password = hash_password(user_update.password)

    db.add(current_user)
    await db.commit()
    await db.refresh(current_user)

    return current_user


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
) -> User:
    """
    Get user by ID.

    Args:
        user_id: User ID
        db: Database session

    Returns:
        User: User information

    Raises:
        HTTPException: If user not found
    """
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


@router.get("", response_model=List[UserResponse])
async def list_users(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
) -> List[User]:
    """
    List all users with pagination.

    Args:
        skip: Number of users to skip
        limit: Maximum number of users to return
        db: Database session

    Returns:
        List[User]: List of users
    """
    result = await db.execute(
        select(User).offset(skip).limit(limit)
    )
    return result.scalars().all()


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_current_user(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> None:
    """
    Deactivate current user account.

    Args:
        current_user: Current authenticated user
        db: Database session
    """
    current_user.is_active = False
    db.add(current_user)
    await db.commit()
