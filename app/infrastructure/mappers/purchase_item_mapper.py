from app.domain.entities.purchase_item import PurchaseItem
from app.infrastructure.database.models.purchase_item_model import PurchaseItemModel

def to_domain(model: PurchaseItemModel) -> PurchaseItem:
    return PurchaseItem(
        id=model.id,
        product_id=model.product_id,
        purchase_id=model.purchase_id,
        quantity=model.quantity,
        unit_price=model.unit_price,
        uploaded_at=model.uploaded_at
    )

def to_model(entity: PurchaseItem) -> PurchaseItemModel:
    return PurchaseItemModel(
        id=entity.id,
        product_id=entity.product_id,
        purchase_id=entity.purchase_id,
        quantity=entity.quantity,
        unit_price=entity.unit_price,
        uploaded_at=entity.uploaded_at
    )
