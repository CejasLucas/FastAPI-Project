from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, field

from app.domain.enums.stock_movement_type import StockMovementType
from app.domain.enums.stock_movement_reference_type import StockMovementReferenceType


@dataclass
class StockMovement:
    id: UUID | None = None

    product_id: UUID | None = None

    reference_id: UUID | None = None

    quantity: int = 0

    movement_type: StockMovementType = StockMovementType.IN

    reference_type: StockMovementReferenceType | None = None

    occurred_at: datetime = field(default_factory=datetime.now)

    @property
    def signed_quantity(self) -> int:
        return -self.quantity if self.movement_type == StockMovementType.OUT else self.quantity