# backend/routers/farm_sites.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import models
import schemas
from dependencies import get_db

router = APIRouter()


@router.post("/", response_model=schemas.FarmSiteResponse)
async def create_farm_site(
    site: schemas.FarmSiteCreate, db: AsyncSession = Depends(get_db)
):
    # Convert Pydantic schema to SQLAlchemy model
    db_site = models.FarmSite(**site.model_dump())

    db.add(db_site)
    await db.commit()
    await db.refresh(db_site)
    return db_site


@router.get("/{site_id}", response_model=schemas.FarmSiteResponse)
async def read_farm_site(site_id: int, db: AsyncSession = Depends(get_db)):
    # Asynchronously query the database for the site
    result = await db.execute(
        select(models.FarmSite).where(models.FarmSite.id == site_id)
    )
    db_site = result.scalars().first()

    if db_site is None:
        raise HTTPException(status_code=404, detail="Farm site not found")

    return db_site
