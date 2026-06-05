from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException

from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.document_repository import SqlAlchemyDocumentRepository

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.get("/")
async def get_documents(
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyDocumentRepository(db)

    return await repo.get_all()


@router.get("/{document_id}")
async def get_document(
    document_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    repo = SqlAlchemyDocumentRepository(db)

    document = await repo.get_by_id(document_id)

    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")

    return document