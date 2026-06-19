import uuid
from uuid import UUID
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy import String, ForeignKey, Integer, Float, DateTime, Enum, func

from app.domain.enums.pruduct_unit import Unit
from app.infrastructure.database.base import Base


class ProductModel(Base):
    __tablename__ = "product"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )

    sku: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    current_stock: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    minimum_stock: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    last_purchase_price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    unit: Mapped[Unit] = mapped_column(
        Enum(Unit),
        nullable=False
    )

    brand_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("brand.id"),
        nullable=True
    )

    category_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("category.id"),
        nullable=True
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    # ── Create objects ────────────────────────────────────────────────────────────────────
    brand = relationship(
        "BrandModel",
        back_populates="products",
    )

    category = relationship(
        "CategoryModel",
        back_populates="products"
    )
