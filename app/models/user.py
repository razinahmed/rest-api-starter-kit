"""
User database model.

Stores user account information with authentication data.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    """
    User model.

    Attributes:
        id: Unique user identifier
        email: User email address (unique)
        hashed_password: Bcrypt hashed password
        full_name: User's full name
        is_active: Whether the user account is active
        created_at: Account creation timestamp
        updated_at: Last update timestamp
        items: Relationship to items owned by user
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    items = relationship("Item", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        """String representation of user."""
        return f"<User(id={self.id}, email={self.email}, full_name={self.full_name})>"
