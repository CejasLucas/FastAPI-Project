from app.domain.entities.category import Category
from app.infrastructure.database.models.category_model import CategoryModel

def to_domain(model: CategoryModel) -> Category:
    return Category(
        id=model.id,
        name=model.name,
        description=model.description,
        uploaded_at=model.uploaded_at
    )


def to_model(entity: Category) -> CategoryModel:
    return CategoryModel(
        id=entity.id,
        name=entity.name,
        description = entity.description,
        uploaded_at=entity.uploaded_at
    )
