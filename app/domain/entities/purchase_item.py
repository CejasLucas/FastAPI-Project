from uuid import UUID
from decimal import Decimal
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class PurchaseItem:
    id: UUID | None = None

    product_id: UUID | None = None

    purchase_id: UUID | None = None

    quantity: int = 0

    unit_price: Decimal = Decimal("0.00")

    uploaded_at: datetime = field(default_factory=datetime.now)

    @property
    def subtotal(self) -> Decimal:
        return self.unit_price * self.quantity