from sqlalchemy import Column, Text, DateTime, UUID, func, String, ForeignKey, JSON, Integer
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.database import Base


class AIMetadata(Base):
    __tablename__ = "ai_metadata"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    link_id = Column(UUID(as_uuid=True), ForeignKey("links.id"), unique=True, nullable=False)
    ai_title = Column(String(200), nullable=True)
    ai_description = Column(Text, nullable=True)
    ai_category = Column(String(50), nullable=True)
    ai_tags = Column(JSON, nullable=True)
    content_summary = Column(Text, nullable=True)
    ai_model_used = Column(String(100), nullable=False)
    processing_time_ms = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    link = relationship("Link", back_populates="ai_metadata")

    def __repr__(self):
        return f"<AIMetadata(link_id={self.link_id}, model={self.ai_model_used})>"