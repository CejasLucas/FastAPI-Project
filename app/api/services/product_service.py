from uuid import UUID
from fastapi import HTTPException

from app.api.dtos.product_dto import (
    ProductDTO,
    ProductCreateDTO,
    ProductUpdateDTO,
    ProductListItemDTO,
)
from app.domain.entities.product import Product
from app.infrastructure.repositories.product_repository import SqlAlchemyProductRepository


class ProductService:
    def __init__(self, repo: SqlAlchemyProductRepository):
        self.repo = repo


    async def get_all(self) -> list[ProductDTO]:

        products = await self.repo.get_all()

        return [ProductDTO.model_validate(p) for p in products]



    async def get_by_id(self, product_id: UUID) -> ProductDTO:

        product = await self.repo.get_by_id(product_id)

        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")

        return ProductDTO.model_validate(product)



    async def get_all_for_selection(self) -> list[ProductListItemDTO]:

        products = await self.repo.get_all_with_details()

        return [
            ProductListItemDTO(
                id=p.id,
                name=p.name,
                unit=p.unit,
                unit_price=float(p.last_purchase_price),
                category_id=p.category_id,
                category=p.category.name if p.category else "—",
                brand_id=p.brand_id,
                brand=p.brand.name if p.brand else "—",
            )
            for p in products
        ]



    async def create(self, dto: ProductCreateDTO) -> ProductDTO:

        product = Product(id=None, **dto.model_dump())

        created = await self.repo.create(product)

        return ProductDTO.model_validate(created)



    async def update(self, product_id: UUID, dto: ProductUpdateDTO) -> ProductDTO:

        existing = await self.repo.get_by_id(product_id)

        if existing is None:
            raise HTTPException(status_code=404, detail="Product not found")

        updated_data = {**vars(existing), **dto.model_dump(exclude_unset=True)}

        updated_product = Product(**updated_data)

        result = await self.repo.update(updated_product)

        return ProductDTO.model_validate(result)



    async def delete(self, product_id: UUID) -> None:

        existing = await self.repo.get_by_id(product_id)

        if existing is None:
            raise HTTPException(status_code=404, detail="Product not found")

        await self.repo.delete(product_id)