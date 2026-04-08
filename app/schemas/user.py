"""
User Pydantic schemas.

Defines request/response schemas for user-related endpoints.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base user schema with common fields."""

    email: EmailStr = Field(..., description="User email address")
    full_name: Optional[str] = Field(None, description="User's full name")


class UserCreate(UserBase):
    """Schema for user registration."""

    password: str = Field(
        ..., min_length=8, description="Password (minimum 8 characters)"
    )


class UserUpdate(BaseModel):
    """Schema for updating user information."""

    full_name: Optional[str] = Field(None, description="User's full name")
    password: Optional[str] = Field(
        None, min_length=8, description="New password (optional)"
    )


class UserResponse(UserBase):
    """Schema for user response."""

    id: int = Field(..., description="User ID")
    is_active: bool = Field(..., description="Whether user is active")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")

    model_config = {"from_attributes": True}


class UserLogin(BaseModel):
    """Schema for user login."""

    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., description="User password")
