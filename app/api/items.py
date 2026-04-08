"""
Item management routes.

Provides CRUD endpoints for item operations with ownership verification.
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse

router = APIRouter()


@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(
    item_data: ItemCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> Item:
    """
    Create a new item owned by current user.

    Args:
        item_data: Item creation data
        current_user: Current authenticated user
        db: Database session

    Returns:
        Item: Created item

    Raises:
        HTTPException: If item creation fails
    """
    new_item = Item(
        title=item_data.title,
        description=item_data.description,
        owner_id=current_user.id,
    )

    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item


@router.get("/my-items", response_model=List[ItemResponse])
async def get_my_items(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
) -> List[Item]:
    """
    Get all items owned by current user.

    Args:
        current_user: Current authenticated user
        db: Database session
        skip: Number of items to skip
        limit: Maximum number of items to return

    Returns:
        List[Item]: List of user's items
    """
    result = await db.execute(
        select(Item)
        .where(Item.owner_id == current_user.id)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
) -> Item:
    """
    Get item by ID.

    Args:
        item_id: Item ID
        db: Database session

    Returns:
        Item: Item information

    Raises:
        HTTPException: If item not found
    """
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalars().first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )

    return item


@router.get("", response_model=List[ItemResponse])
async def list_items(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
) -> List[Item]:
    """
    List all items with pagination.

    Args:
        skip: Number of items to skip
        limit: Maximum number of items to return
        db: Database session

    Returns:
        List[Item]: List of items
    """
    result = await db.execute(
        select(Item).offset(skip).limit(limit)
    )
    return result.scalars().all()


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: int,
    item_update: ItemUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> Item:
    """
    Update an item (only owner can update).

    Args:
        item_id: Item ID
        item_update: Item update data
        current_user: Current authenticated user
        db: Database session

    Returns:
        Item: Updated item

    Raises:
        HTTPException: If item not found or user is not owner
    """
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalars().first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )

    if item.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only update your own items",
        )

    if item_update.title is not None:
        item.title = item_update.title

    if item_update.description is not None:
        item.description = item_update.description

    db.add(item)
    await db.commit()
    await db.refresh(item)

    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> None:
    """
    Delete an item (only owner can delete).

    Args:
        item_id: Item ID
        current_user: Current authenticated user
        db: Database session

    Raises:
        HTTPException: If item not found or user is not owner
    """
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalars().first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )

    if item.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own items",
        )

    await db.delete(item)
    await db.commit()
