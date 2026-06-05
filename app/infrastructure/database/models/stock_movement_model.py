import uuid
from uuid import UUID
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, DateTime, ForeignKey, Enum, func

from app.infrastructure.database.base import Base
from app.domain.enums.stock_movement_type import StockMovementType


class StockMovementModel(Base):
    __tablename__ = "stock_movement"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )

    product_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("product.id"),
        nullable=False
    )

    reference_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        nullable=True
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    movement_type: Mapped[StockMovementType] = mapped_column(
        Enum(StockMovementType),
        nullable=False
    )

    reference_type: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    occurred_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    product = relationship("ProductModel", backref="stock_movements")