from app.domain.entities.product import Product
from app.infrastructure.database.models.product_model import ProductModel

def to_domain(model: ProductModel) -> Product:
    return Product(
        id=model.id,
        sku=model.sku,
        name=model.name,
        description=model.description,
        current_stock=model.current_stock,
        minimum_stock=model.minimum_stock,
        last_purchase_price=model.last_purchase_price,
        unit=model.unit,
        category_id=model.category_id,
        uploaded_at=model.uploaded_at
    )


def to_model(entity: Product) -> ProductModel:
    return ProductModel(
        id=entity.id,
        sku=entity.sku,
        name=entity.name,
        description=entity.description,
        current_stock=entity.current_stock,
        minimum_stock=entity.minimum_stock,
        last_purchase_price=entity.last_purchase_price,
        unit=entity.unit,
        category_id=entity.category_id,
        uploaded_at=entity.uploaded_at
    )
