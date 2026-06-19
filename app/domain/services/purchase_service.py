from uuid import UUID
from fastapi import HTTPException

from api.dtos.purchase_dto import (
    PurchaseItemProductDTO,
    PurchaseItemDetailDTO,
    PurchaseSupplierDetailDTO,
    PurchaseDetailDTO
)
from app.domain.repositories.purchase_repository import PurchaseRepository


class PurchaseService:
    def __init__(self, repo: PurchaseRepository):
        self.repo = repo

    async def get_detail(self, purchase_id: UUID) -> PurchaseDetailDTO:
        purchase = await self.repo.get_detail(purchase_id)

        if purchase is None:
            raise HTTPException(status_code=404, detail="Purchase not found")

        return PurchaseDetailDTO(
            id=purchase.id,
            purchase_date=purchase.purchase_date,
            status=purchase.status,
            total_amount=float(purchase.total_amount),
            supplier=PurchaseSupplierDetailDTO(
                supplier_id=purchase.supplier.id,
                name=purchase.supplier.name,
                email=purchase.supplier.email,
                phone=purchase.supplier.phone,
                address=purchase.supplier.address,
                locality=purchase.supplier.locality,
                nationality=purchase.supplier.nationality,
                tax_id=purchase.supplier.tax_id,
            ),
            items=[
                PurchaseItemDetailDTO(
                    quantity=item.quantity,
                    unit_price=float(item.unit_price),
                    subtotal=float(item.quantity * item.unit_price),
                    product=PurchaseItemProductDTO(
                        product_id=item.product.id,
                        name=item.product.name,
                        brand=item.product.brand.name,
                        category=item.product.category.name,
                    )
                )
                for item in purchase.items
            ]
        )
