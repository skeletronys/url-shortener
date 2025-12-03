from sqlalchemy import Column, Text, Boolean, DateTime, UUID, func, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.database import Base

class DeviceTypeEnum(str):
    MOBILE = "mobile"
    DESKTOP = "desktop"
    TABLET = "tablet"

class Click(Base):
    __tablename__ = "clicks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    link_id = Column(UUID(as_uuid=True), ForeignKey("links.id"))
    ip_address = Column(String(45), nullable=False)
    user_agent = Column(Text, nullable=False)
    referer = Column(String(500), nullable=False)
    country = Column(String(3), nullable=False)
    city = Column(String(100), nullable=False)
    device_type = Column(
        Enum(
            DeviceTypeEnum.MOBILE,
            DeviceTypeEnum.DESKTOP,
            DeviceTypeEnum.TABLET,
            name="device_type_enum"
        ),
        nullable=True)
    browser = Column(String(50), nullable=False)
    os = Column(String(50), nullable=False)
    clicked_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    clicks = relationship("Click", back_populates="link")
