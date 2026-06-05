from app.domain.entities.purchase import Purchase
from app.infrastructure.database.models.purchase_model import PurchaseModel

def to_domain(model: PurchaseModel) -> Purchase:
    return Purchase(
        id=model.id,
        total_amount=model.total_amount,
        status=model.status,
        purchase_date=model.purchase_date,
        supplier_id=model.supplier_id,
        uploaded_at=model.uploaded_at
    )

def to_model(entity: Purchase) -> PurchaseModel:
    return PurchaseModel(
        id=entity.id,
        total_amount=entity.total_amount,
        status=entity.status,
        purchase_date=entity.purchase_date,
        supplier_id=entity.supplier_id,
        uploaded_at=entity.uploaded_at
    )
