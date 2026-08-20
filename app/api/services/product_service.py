from app.api.dtos.product_dto import ProductListItemDTO
from app.infrastructure.repositories.product_repository import SqlAlchemyProductRepository

class ProductService:
    def __init__(self, repo: SqlAlchemyProductRepository):
        self.repo = repo

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