from sqlalchemy import Column, Text, Boolean, DateTime, UUID, func, String, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.database import Base


class Link(Base):
    __tablename__ = "links"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    original_url = Column(Text)
    short_code = Column(String(10), unique=True)
    custom_alias = Column(String(50), nullable=False, unique=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50), nullable=False)
    expires_at = Column(DateTime, nullable=False)
    as_active = Column(Boolean, default=True)
    ai_generation = Column(Boolean, default=False)
    used_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    user = relationship("User", back_populates="links")
    clicks = relationship("Click", back_populates="link", cascade="all, delete-orphan")
    ai_metadata = relationship("AIMetadata", back_populates="link", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Link(id={self.id}, short_code={self.short_code})>"