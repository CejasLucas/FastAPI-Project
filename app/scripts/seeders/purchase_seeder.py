from datetime import datetime
from app.domain.entities.purchase import Purchase
from app.domain.enums.purchase_status import PurchaseStatus


def build_purchases(supplier_map) -> list[Purchase]:
    return [
        Purchase(
            supplier_id=supplier_map["BOSCH"].id,
            total_amount=980000.0,
            purchase_date=datetime(2026, 1, 15),
            status=PurchaseStatus.CONFIRMED,
        ),
        Purchase(
            supplier_id=supplier_map["DELPHI"].id,
            total_amount=3018000.0,
            purchase_date=datetime(2026, 2, 12),
            status=PurchaseStatus.CONFIRMED,
        ),
        Purchase(
            supplier_id=supplier_map["KYB"].id,
            total_amount=1411000.0,
            purchase_date=datetime(2026, 3, 18),
            status=PurchaseStatus.CONFIRMED,
        ),
        Purchase(
            supplier_id=supplier_map["BYD AUTO PARTS"].id,
            total_amount=2900000.0,
            purchase_date=datetime(2026, 4, 10),
            status=PurchaseStatus.CONFIRMED,
        ),
        Purchase(
            supplier_id=supplier_map["BOSCH"].id,
            total_amount=1650000.0,
            purchase_date=datetime(2026, 5, 14),
            status=PurchaseStatus.CONFIRMED,
        ),
        Purchase(
            supplier_id=supplier_map["DELPHI"].id,
            total_amount=2240000.0,
            purchase_date=datetime(2026, 6, 20),
            status=PurchaseStatus.CONFIRMED,
        ),
        Purchase(
            supplier_id=supplier_map["KYB"].id,
            total_amount=1890000.0,
            purchase_date=datetime(2026, 7, 15),
            status=PurchaseStatus.PENDING,
        ),
        # PENDING
        Purchase(
            supplier_id=supplier_map["BRIDGESTONE"].id,
            total_amount=3440000.0,
            purchase_date=datetime(2026, 8, 8),
            status=PurchaseStatus.PENDING,
        ),
        Purchase(
            supplier_id=supplier_map["BOSCH"].id,
            total_amount=2174000.0,
            purchase_date=datetime(2026, 9, 10),
            status=PurchaseStatus.PENDING,
        ),
        Purchase(
            supplier_id=supplier_map["MICHELIN"].id,
            total_amount=3985000.0,
            purchase_date=datetime(2026, 10, 7),
            status=PurchaseStatus.PENDING,
        ),
        Purchase(
            supplier_id=supplier_map["DELPHI"].id,
            total_amount=4120000.0,
            purchase_date=datetime(2026, 11, 12),
            status=PurchaseStatus.PENDING,
        ),
        Purchase(
            supplier_id=supplier_map["GOODYEAR"].id,
            total_amount=5236000.0,
            purchase_date=datetime(2026, 12, 3),
            status=PurchaseStatus.PENDING,
        ),
    ]