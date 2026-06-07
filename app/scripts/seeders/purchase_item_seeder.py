from decimal import Decimal

from app.domain.entities.purchase_item import PurchaseItem


def build_purchase_items(purchases, product_map) -> list[PurchaseItem]:
    return [
        # COMPRA 1
        PurchaseItem(
            purchase_id=purchases[0].id,
            product_id=product_map["FIL-001"].id,
            quantity=20,
            unit_price=Decimal("12000")
        ),
        PurchaseItem(
            purchase_id=purchases[0].id,
            product_id=product_map["FIL-002"].id,
            quantity=15,
            unit_price=Decimal("14000")
        ),
        PurchaseItem(
            purchase_id=purchases[0].id,
            product_id=product_map["BRA-001"].id,
            quantity=10,
            unit_price=Decimal("28000")
        ),
        PurchaseItem(
            purchase_id=purchases[0].id,
            product_id=product_map["ELE-001"].id,
            quantity=50,
            unit_price=Decimal("5000")
        ),

        # COMPRA 2
        PurchaseItem(
            purchase_id=purchases[1].id,
            product_id=product_map["SUS-001"].id,
            quantity=8,
            unit_price=Decimal("85000")
        ),
        PurchaseItem(
            purchase_id=purchases[1].id,
            product_id=product_map["SUS-002"].id,
            quantity=10,
            unit_price=Decimal("79000")
        ),
        PurchaseItem(
            purchase_id=purchases[1].id,
            product_id=product_map["ENG-001"].id,
            quantity=12,
            unit_price=Decimal("58000")
        ),
        PurchaseItem(
            purchase_id=purchases[1].id,
            product_id=product_map["ENG-002"].id,
            quantity=6,
            unit_price=Decimal("72000")
        ),
        PurchaseItem(
            purchase_id=purchases[1].id,
            product_id=product_map["COL-001"].id,
            quantity=3,
            unit_price=Decimal("140000")
        ),

        # COMPRA 3
        PurchaseItem(
            purchase_id=purchases[2].id,
            product_id=product_map["STE-001"].id,
            quantity=15,
            unit_price=Decimal("21000")
        ),
        PurchaseItem(
            purchase_id=purchases[2].id,
            product_id=product_map["STE-002"].id,
            quantity=12,
            unit_price=Decimal("23000")
        ),
        PurchaseItem(
            purchase_id=purchases[2].id,
            product_id=product_map["SEN-001"].id,
            quantity=10,
            unit_price=Decimal("38000")
        ),
        PurchaseItem(
            purchase_id=purchases[2].id,
            product_id=product_map["SEN-002"].id,
            quantity=8,
            unit_price=Decimal("55000")
        ),

        # COMPRA 4
        PurchaseItem(
            purchase_id=purchases[3].id,
            product_id=product_map["BAT-001"].id,
            quantity=10,
            unit_price=Decimal("125000")
        ),
        PurchaseItem(
            purchase_id=purchases[3].id,
            product_id=product_map["LIG-001"].id,
            quantity=40,
            unit_price=Decimal("7000")
        ),
        PurchaseItem(
            purchase_id=purchases[3].id,
            product_id=product_map["WIP-001"].id,
            quantity=30,
            unit_price=Decimal("12000")
        ),
        PurchaseItem(
            purchase_id=purchases[3].id,
            product_id=product_map["CHI-001"].id,
            quantity=20,
            unit_price=Decimal("13000")
        ),
        PurchaseItem(
            purchase_id=purchases[3].id,
            product_id=product_map["CHI-002"].id,
            quantity=15,
            unit_price=Decimal("24000")
        ),
        PurchaseItem(
            purchase_id=purchases[3].id,
            product_id=product_map["CHI-003"].id,
            quantity=10,
            unit_price=Decimal("39000")
        ),
    ]