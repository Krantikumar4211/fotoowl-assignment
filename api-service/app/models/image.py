from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    google_drive_id = Column(String, nullable=False)
    size = Column(BigInteger)
    mime_type = Column(String)
    storage_path = Column(String)
    source = Column(String, default="google_drive")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
