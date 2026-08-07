# backend/models.py
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from database import Base


class FarmSite(Base):
    __tablename__ = "farm_sites"

    id = Column(Integer, primary_key=True, index=True)
    site_name = Column(String, index=True)
    location_coordinates = Column(String)
    soil_type = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
