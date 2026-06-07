# DOMAIN
from app.domain.entities.brand import Brand
from app.domain.repositories.brand_repository import BrandRepository

# DATABASE
from app.infrastructure.database.session import AsyncSession
from app.infrastructure.database.models.brand_model import BrandModel

# INFRASTRUCTURE
from app.infrastructure.repositories.base_repository import SqlAlchemyBaseRepository
from app.infrastructure.mappers.brand_mapper import to_domain, to_model


class SqlAlchemyBrandRepository(
    SqlAlchemyBaseRepository[Brand, BrandModel],
    BrandRepository
):

    def __init__(self, session: AsyncSession):
        super().__init__(
            session=session,
            model=BrandModel,
            to_domain=to_domain,
            to_model=to_model
        )