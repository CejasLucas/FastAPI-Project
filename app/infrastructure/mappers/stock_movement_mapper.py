from app.domain.entities.stock_movement import StockMovement
from app.infrastructure.database.models.stock_movement_model import StockMovementModel

def to_domain(model: StockMovementModel) -> StockMovement:
    return StockMovement(
        id=model.id,
        product_id=model.product_id,
        reference_id=model.reference_id,
        quantity=model.quantity,
        movement_type=model.movement_type,
        reference_type=model.reference_type,
        occurred_at=model.occurred_at
    )

def to_model(entity: StockMovement) -> StockMovementModel:
    return StockMovementModel(
        id=entity.id,
        product_id=entity.product_id,
        reference_id=entity.reference_id,
        quantity=entity.quantity,
        movement_type=entity.movement_type,
        reference_type=entity.reference_type,
        occurred_at=entity.occurred_at
    )
