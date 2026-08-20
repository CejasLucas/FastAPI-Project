from uuid import UUID
from pydantic import BaseModel
from app.domain.enums.pruduct_unit import Unit

# ── Schemas ────────────────────────────────────────────────────────────────────
class ProductCreateDTO(BaseModel):
    sku: str
    name: str
    description: str
    current_stock: int
    minimum_stock: int
    last_purchase_price: int
    unit: Unit
    brand_id: UUID
    category_id: UUID

class ProductUpdateDTO(BaseModel):
    sku: str | None = None
    name: str | None = None
    description: str | None = None
    current_stock: int = 0
    minimum_stock: int = 0
    last_purchase_price: int = 0
    unit: Unit = Unit.UNIT
    brand_id: UUID
    category_id: UUID


class ProductListItemDTO(BaseModel):
    id: UUID
    name: str
    unit: Unit
    unit_price: float
    category_id: UUID
    category: str
    brand_id: UUID
    brand: str
