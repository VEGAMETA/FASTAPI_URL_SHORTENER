from sqlalchemy import Column, Integer, String, DateTime, func
from .base import Base


class URL(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, unique=True, index=True)
    short_url = Column(String, unique=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
