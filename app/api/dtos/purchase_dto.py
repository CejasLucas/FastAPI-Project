from typing import Any
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

from app.domain.enums.purchase_status import PurchaseStatus

class PurchaseDetailDTO(BaseModel):
    id: UUID
    supplier_id: UUID
    purchase_date: datetime
    status: PurchaseStatus
    total_amount: float
    items: list[dict[str, Any]]