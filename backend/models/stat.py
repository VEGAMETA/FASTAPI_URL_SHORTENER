from sqlalchemy import Column, Integer, DateTime, func
from .base import Base


class StatURL(Base):
    __tablename__ = "stats"
    id = Column(Integer, primary_key=True, index=True)
    url_id = Column(Integer)
    redirected_at = Column(DateTime, server_default=func.now())
