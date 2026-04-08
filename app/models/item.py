"""
Item database model.

Stores items owned by users with basic metadata.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Item(Base):
    """
    Item model.

    Attributes:
        id: Unique item identifier
        title: Item title
        description: Detailed item description
        owner_id: Foreign key to User (owner)
        created_at: Item creation timestamp
        owner: Relationship to User model
    """

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    owner = relationship("User", back_populates="items")

    def __repr__(self) -> str:
        """String representation of item."""
        return f"<Item(id={self.id}, title={self.title}, owner_id={self.owner_id})>"
