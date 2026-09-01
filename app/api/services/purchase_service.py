from uuid import UUID

from fastapi import HTTPException

from app.api.dtos.purchase_dto import (
    PurchaseDetailDTO,
    PurchaseSupplierDetailDTO,
    PurchaseItemDetailDTO,
    PurchaseItemProductDTO,
    PurchaseListItemDTO,
    PurchaseCreateDTO,
    PurchaseUpdateDTO,
)
from app.domain.repositories.purchase_repository import PurchaseRepository


class PurchaseService:
    def __init__(self, repo: PurchaseRepository):
        self.repo = repo


    async def get_all(self) -> list[PurchaseListItemDTO]:

        purchases = await self.repo.get_all_with_details()

        return [
            PurchaseListItemDTO(
                id=p.id,
                purchase_date=p.purchase_date,
                status=p.status,
                total_amount=float(p.total_amount),
                supplier_name=p.supplier.name if p.supplier else "—",
                items_count=len(p.items),
            )
            for p in purchases
        ]



    async def get_detail(self, purchase_id: UUID) -> PurchaseDetailDTO:

        purchase = await self.repo.get_detail_model(purchase_id)

        if purchase is None:
            raise HTTPException(status_code=404, detail="Purchase not found")

        return self._to_detail_dto(purchase)



    async def create(self, dto: PurchaseCreateDTO) -> PurchaseDetailDTO:

        items = [item.model_dump() for item in dto.items]

        purchase = await self.repo.create_full(
            supplier_id=dto.supplier_id,
            purchase_date=dto.purchase_date,
            status=dto.status,
            items=items,
        )

        return await self.get_detail(purchase.id)



    async def update(self, purchase_id: UUID, dto: PurchaseUpdateDTO) -> PurchaseDetailDTO:

        items = [item.model_dump() for item in dto.items]

        purchase = await self.repo.update_full(
            purchase_id=purchase_id,
            supplier_id=dto.supplier_id,
            purchase_date=dto.purchase_date,
            status=dto.status,
            items=items,
        )

        if purchase is None:
            raise HTTPException(status_code=404, detail="Purchase not found")

        return await self.get_detail(purchase_id)



    async def delete(self, purchase_id: UUID) -> None:

        deleted = await self.repo.delete_by_id(purchase_id)

        if not deleted:
            raise HTTPException(status_code=404, detail="Purchase not found")



    def _to_detail_dto(self, purchase) -> PurchaseDetailDTO:
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
                    ),
                )
                for item in purchase.items
            ],
        )