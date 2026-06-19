from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

from app.domain.enums.purchase_status import PurchaseStatus

class PurchaseItemProductDTO(BaseModel):
    product_id: UUID
    name: str
    brand: str
    category: str

class PurchaseItemDetailDTO(BaseModel):
    quantity: int
    unit_price: float
    subtotal: float
    product: PurchaseItemProductDTO

class PurchaseSupplierDetailDTO(BaseModel):
    supplier_id: UUID
    name: str
    email: str
    phone: str
    address: str
    locality: str
    nationality: str
    tax_id: str

class PurchaseDetailDTO(BaseModel):
    id: UUID
    purchase_date: datetime
    status: PurchaseStatus
    total_amount: float
    supplier: PurchaseSupplierDetailDTO
    items: list[PurchaseItemDetailDTO]