from sqlalchemy import select

from app.domain.entities.product import Product
from app.domain.repositories.product_repository import ProductRepository

from app.infrastructure.database.session import AsyncSession
from app.infrastructure.database.models.product_model import ProductModel

from app.infrastructure.mappers.product_mapper import to_domain, to_model
from app.infrastructure.repositories.base_repository import SqlAlchemyBaseRepository


class SqlAlchemyProductRepository(
    SqlAlchemyBaseRepository[Product, ProductModel],
    ProductRepository
):

    def __init__(self, session: AsyncSession):
        super().__init__(
            session=session,
            model=ProductModel,
            to_domain=to_domain,
            to_model=to_model
        )


    async def get_low_stock(self, limit: int) -> list[Product]:
        stmt = (
            select(ProductModel)
            .where(
                ProductModel.current_stock <= ProductModel.minimum_stock
            )
            .order_by(
                ProductModel.current_stock.asc()
            )
            .limit(limit)
        )

        result = await self.session.execute(stmt)
        products = result.scalars().all()

        return [self.to_domain(product) for product in products]
