"""
Token Pydantic schemas.

Defines request/response schemas for authentication tokens.
"""
from pydantic import BaseModel, Field


class TokenResponse(BaseModel):
    """Schema for token response."""

    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="Token type")


class TokenRefresh(BaseModel):
    """Schema for token refresh request."""

    refresh_token: str = Field(..., description="Refresh token")
