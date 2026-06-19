import uuid
from uuid import UUID
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy import String, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.base import Base


class DocumentModel(Base):
    __tablename__ = "document"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    file_url: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    filename: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    purchase_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("purchase.id"),
        nullable=True
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    # ── Create objects ────────────────────────────────────────────────────────────────────
    purchase = relationship(
        "PurchaseModel",
        back_populates="documents"
    )