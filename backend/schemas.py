from pydantic import BaseModel, ConfigDict
from typing import Optional

# Base properties shared across schemas
class FarmSiteBase(BaseModel):
    site_name: str
    location: Optional[str] = None
    # Add other fields like acreage, coordinates, etc.

# Schema for creating a new site (what the user sends)
class FarmSiteCreate(FarmSiteBase):
    pass

# Schema for reading a site (what the API returns)
class FarmSiteResponse(FarmSiteBase):
    id: int

    # This tells Pydantic to read the data even if it's an SQLAlchemy model
    model_config = ConfigDict(from_attributes=True)