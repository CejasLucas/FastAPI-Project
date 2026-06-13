from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class PurchaseItem:
    id: UUID | None = None

    product_id: UUID | None = None

    purchase_id: UUID | None = None

    quantity: int = 0

    unit_price: float = 0.0

    uploaded_at: datetime = field(default_factory=datetime.now)

    @property
    def subtotal(self) -> float:
        return self.unit_price * self.quantity