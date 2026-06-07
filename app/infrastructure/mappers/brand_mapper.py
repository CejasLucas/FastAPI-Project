from app.domain.entities.brand import Brand
from app.infrastructure.database.models.brand_model import BrandModel

def to_domain(model: BrandModel) -> Brand:
    return Brand(
        id=model.id,
        name=model.name,
        active=model.active,
        nationality=model.nationality,
        uploaded_at=model.uploaded_at
    )


def to_model(entity: Brand) -> BrandModel:
    return BrandModel(
        id=entity.id,
        name=entity.name,
        active=entity.active,
        nationality=entity.nationality,
        uploaded_at=entity.uploaded_at
    )
