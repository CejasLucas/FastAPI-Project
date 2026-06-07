from datetime import datetime
from app.domain.entities.purchase import Purchase
from app.domain.enums.purchase_status import PurchaseStatus


def build_purchases(supplier_map) -> list[Purchase]:
    return [
        Purchase(
            supplier_id=supplier_map["BOSCH"].id,
            total_amount=490000.0,
            purchase_date=datetime.utcnow(),
            status=PurchaseStatus.CONFIRMED,
        ),
        Purchase(
            supplier_id=supplier_map["DELPHI"].id,
            total_amount=725000.0,
            purchase_date=datetime.utcnow(),
            status=PurchaseStatus.CONFIRMED,
        ),
        Purchase(
            supplier_id=supplier_map["KYB"].id,
            total_amount=315000.0,
            purchase_date=datetime.utcnow(),
            status=PurchaseStatus.PENDING,
        ),
        Purchase(
            supplier_id=supplier_map["BYD AUTO PARTS"].id,
            total_amount=980000.0,
            purchase_date=datetime.utcnow(),
            status=PurchaseStatus.CONFIRMED,
        ),
    ]