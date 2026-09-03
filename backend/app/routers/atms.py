from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.schemas.atm import ATMRead, ATMCreate
from app.dependencies import get_db, get_current_user, require_role
from app.models import ATM, User, Technician_RBAC, Technician
from app.models.enums import ATMStatus

router = APIRouter(prefix="/atms", tags=["atms"])

@router.get("", response_model = list[ATMRead])
async def list_atms(db: AsyncSession = Depends(get_db), _: User = Depends(get_current_user)):
    statement = select(ATM).where(ATM.status != ATMStatus.OFFLINE)
    result = await db.execute(statement)
    return list(result.scalars().all())

@router.get("/low_cash", response_model = list[ATMRead])
async def active_atms_with_low_cash(low_cash_threshold: int = 20, db: AsyncSession = Depends(get_db), _: User = Depends(get_current_user)):
    statement = select(ATM).where(ATM.cash_level, low_cash_threshold).where(ATM.status != ATMStatus.OFFLINE)
    result = await db.execute(statement)
    return list(result.scalars().all())

@router.get("/atm_id", response_model=ATMRead)
async def get_atm(atm_id: int, db: AsyncSession = Depends(get_db), _: User = Depends(get_current_user)) -> ATM:
    atm = await db.get(ATM, atm_id)
    if atm is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ATM with {atm_id} not found"
        )
    return atm
