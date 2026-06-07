from app.domain.entities.stock_movement import StockMovement
from app.domain.enums.stock_movement_type import StockMovementType
from app.domain.enums.stock_movement_reference_type import StockMovementReferenceType


def build_stock_movements(purchase_items) -> list[StockMovement]:
    return [
        StockMovement(
            product_id=item.product_id,
            reference_id=item.purchase_id,
            quantity=item.quantity,
            movement_type=StockMovementType.IN,
            reference_type=StockMovementReferenceType.PURCHASE
        )
        for item in purchase_items
    ]