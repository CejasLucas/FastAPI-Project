import uuid
from uuid import UUID
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey, Enum, Numeric, func

from app.infrastructure.database.base import Base
from app.domain.enums.purchase_status import PurchaseStatus
from app.infrastructure.database.models.document_model import DocumentModel


class PurchaseModel(Base):
    __tablename__ = "purchase"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    total_amount: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    status: Mapped[PurchaseStatus] = mapped_column(
        Enum(PurchaseStatus),
        nullable=False
    )

    purchase_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    supplier_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("supplier.id"),
        nullable=True
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    documents: Mapped[list[DocumentModel]] = relationship(
        "DocumentModel",
        back_populates="purchase",
        cascade="all, delete-orphan"
    )

    # ── Create objects ────────────────────────────────────────────────────────────────────
    supplier = relationship(
        "SupplierModel",
        back_populates="purchases"
    )

    items = relationship(
        "PurchaseItemModel",
        backref="purchase",
        cascade="all, delete-orphan"
    )