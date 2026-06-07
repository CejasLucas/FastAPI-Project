from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, field

from app.domain.enums.pruduct_unit import Unit


@dataclass
class Product:
    id: UUID | None = None

    sku: str = ""

    name: str = ""

    description: str = ""

    current_stock: int = 0

    minimum_stock: int = 0

    last_purchase_price: float = 0.0

    unit: Unit = Unit.UNIT

    brand_id: UUID | None = None

    category_id: UUID | None = None

    uploaded_at: datetime = field(default_factory=datetime.now)