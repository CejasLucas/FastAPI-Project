from uuid import UUID
from pydantic import BaseModel, ConfigDict
from app.domain.enums.pruduct_unit import Unit


class ProductCreateDTO(BaseModel):
    sku: str
    name: str
    description: str
    current_stock: int
    minimum_stock: int
    last_purchase_price: float
    unit: Unit
    brand_id: UUID
    category_id: UUID


class ProductUpdateDTO(BaseModel):
    sku: str | None = None
    name: str | None = None
    description: str | None = None
    current_stock: int | None = None
    minimum_stock: int | None = None
    last_purchase_price: float | None = None
    unit: Unit | None = None
    brand_id: UUID | None = None
    category_id: UUID | None = None


class ProductDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    sku: str
    name: str
    description: str
    current_stock: int
    minimum_stock: int
    last_purchase_price: float
    unit: Unit
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