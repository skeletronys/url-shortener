from sqlalchemy import Column, Text, Boolean, DateTime, UUID, func, String, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.database import Base


class Click(Base):
    __tablename__ = "clicks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    lin