from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.session import get_session

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check(
    db: AsyncSession = Depends(get_session),
):
    try:
        await db.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "database": "connected",
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "error",
                "database": "disconnected",
            },
        )