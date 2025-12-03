from sqlalchemy import Column, Text, DateTime, UUID, func, String, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.database import Base


class Click(Base):
    __tablename__ = "clicks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    link_id = Column(UUID(as_uuid=True), ForeignKey("links.id"), nullable=False)
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(Text, nullable=True)
    referer = Column(String(500), nullable=True)
    country = Column(String(3), nullable=True)
    city = Column(String(100), nullable=True)
    device_type = Column(String(20), nullable=True)
    browser = Column(String(50), nullable=True)
    os = Column(String(50), nullable=True)
    clicked_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    link = relationship("Link", back_populates="clicks")

    def __repr__(self):
        return f"<Click(id={self.id}, link_id={self.link_id}, country={self.country})>"