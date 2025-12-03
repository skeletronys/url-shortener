from sqlalchemy import Column, Text, Boolean, DateTime, UUID, func, String, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy import Enum as SQLEnum

from app.database import Base

class DeviceTypeEnum(str):
    MOBILE = "mobile"
    DESKTOP = "desktop"
    TABLET = "tablet"

class Click(Base):
    __tablename__ = "clicks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    link_id = Column(UUID(as_uuid=True), ForeignKey("links.id"))
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(Text, nullable=True)
    referer = Column(String(500), nullable=True)
    country = Column(String(3), nullable=True)
    city = Column(String(100), nullable=True)
    device_type = Column(SQLEnum("mobile", "desktop", "tablet", name="device_type_enum"), nullable=True)
    browser = Column(String(50), nullable=True)
    os = Column(String(50), nullable=True)
    clicked_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    link = relationship("Link", back_populates="clicks")
