from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, field

from app.domain.enums.purchase_status import PurchaseStatus


@dataclass
class Purchase:
    id: UUID | None = None

    total_amount: float = 0.0

    status: PurchaseStatus = PurchaseStatus.CONFIRMED

    purchase_date: datetime = field(default_factory=datetime.now)

    supplier_id: UUID | None = None

    uploaded_at: datetime = field(default_factory=datetime.now)