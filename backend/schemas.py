from pydantic import BaseModel, ConfigDict


class FarmSiteBase(BaseModel):
    site_name: str
    location_coordinates: str | None = None
    soil_type: str | None = None


class FarmSiteCreate(FarmSiteBase):
    pass


class FarmSiteResponse(FarmSiteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
