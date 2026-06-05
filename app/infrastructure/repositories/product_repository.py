# DOMAIN
from app.domain.entities.product import Product
from app.domain.repositories.product_repository import ProductRepository

# DATABASE
from app.infrastructure.database.session import AsyncSession
from app.infrastructure.database.models.product_model import ProductModel

# INFRASTRUCTURE
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
