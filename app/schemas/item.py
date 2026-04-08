"""
Item Pydantic schemas.

Defines request/response schemas for item-related endpoints.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    """Base item schema with common fields."""

    title: str = Field(..., min_length=1, max_length=255, description="Item title")
    description: Optional[str] = Field(None, description="Item description")


class ItemCreate(ItemBase):
    """Schema for creating a new item."""

    pass


class ItemUpdate(BaseModel):
    """Schema for updating an item."""

    title: Optional[str] = Field(None, min_length=1, max_length=255, description="Item title")
    description: Optional[str] = Field(None, description="Item description")


class ItemResponse(ItemBase):
    """Schema for item response."""

    id: int = Field(..., description="Item ID")
    owner_id: int = Field(..., description="Owner user ID")
    created_at: datetime = Field(..., description="Creation timestamp")

    model_config = {"from_attributes": True}
