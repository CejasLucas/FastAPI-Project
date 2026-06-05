from enum import StrEnum

class StockMovementReferenceType(StrEnum):
    SALE = "sale"
    DAMAGE = "damage"
    PURCHASE = "purchase"
    ADJUSTMENT = "adjustment"