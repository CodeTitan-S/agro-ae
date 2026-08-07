from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

import models
import schemas
from database import get_db
from routers import farm_sites

app = FastAPI(title="AgroAE API")

app.include_router(farm_sites.router, prefix="/api/v1/sites", tags=["Farm Sites"])


@app.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    return {"status": "healthy", "database": "connected"}


@app.post("/sites/", response_model=schemas.FarmSiteResponse)
async def create_farm_site(
    site: schemas.FarmSiteCreate, db: AsyncSession = Depends(get_db)
):
    # Create the SQLAlchemy model instance
    db_site = models.FarmSite(**site.model_dump())

    # Add and commit to the database
    db.add(db_site)
    await db.commit()
    await db.refresh(db_site)

    return db_site


@app.get("/")
async def root():
    return {"message": "Welcome to the Agro-AE API"}
