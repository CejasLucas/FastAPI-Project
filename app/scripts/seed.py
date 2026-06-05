import asyncio
from datetime import datetime
from decimal import Decimal

from app.infrastructure.database.session import SessionLocal

from app.domain.enums.pruduct_unit import Unit
from app.domain.enums.purchase_status import PurchaseStatus
from app.domain.enums.stock_movement_type import StockMovementType
from app.domain.enums.stock_movement_reference_type import StockMovementReferenceType

from app.domain.entities.category import Category
from app.domain.entities.document import Document
from app.domain.entities.product import Product
from app.domain.entities.supplier import Supplier
from app.domain.entities.purchase import Purchase
from app.domain.entities.purchase_item import PurchaseItem
from app.domain.entities.stock_movement import StockMovement

from app.infrastructure.repositories.category_repository import SqlAlchemyCategoryRepository
from app.infrastructure.repositories.document_repository import SqlAlchemyDocumentRepository
from app.infrastructure.repositories.product_repository import SqlAlchemyProductRepository
from app.infrastructure.repositories.purchase_repository import SqlAlchemyPurchaseRepository
from app.infrastructure.repositories.purchase_item_repository import SqlAlchemyPurchaseItemRepository
from app.infrastructure.repositories.supplier_repository import SqlAlchemySupplierRepository
from app.infrastructure.repositories.stock_movement_repository import SqlAlchemyStockMovementRepository



async def seed():

    async with SessionLocal() as db:

        repo_supplier = SqlAlchemySupplierRepository(db)
        repo_category = SqlAlchemyCategoryRepository(db)
        repo_product = SqlAlchemyProductRepository(db)
        repo_document = SqlAlchemyDocumentRepository(db)
        repo_purchase = SqlAlchemyPurchaseRepository(db)
        repo_purchase_item = SqlAlchemyPurchaseItemRepository(db)
        repo_stock = SqlAlchemyStockMovementRepository(db)

        try:
            # ---------------- SUPPLIER ----------------
            supplier = await repo_supplier.create(
                Supplier(
                    name="Pirelli Argentina",
                    email="contacto@pirelli.com",
                    phone="123456789",
                    tax_id="30-45684512-4"
                )
            )

            # ---------------- CATEGORY ----------------
            category = await repo_category.create(
                Category(
                    name="Filtros",
                    description="Componentes de filtrado para motor"
                )
            )

            # ---------------- PRODUCT ----------------
            product = await repo_product.create(
                Product(
                    sku="FILT-001",
                    name="Filtro de aceite Pirelli",
                    description="Filtro de alto rendimiento",
                    current_stock=0,
                    minimum_stock=10,
                    last_purchase_price=10000.0,
                    unit=Unit.UNIT,
                    category_id=category.id
                )
            )

            # ---------------- PURCHASE ----------------
            purchase = await repo_purchase.create(
                Purchase(
                    total_amount=16300.00,
                    status=PurchaseStatus.CONFIRMED,
                    purchase_date=datetime.utcnow(),
                    supplier_id = supplier.id
                )
            )

            # ---------------- PURCHASE ITEM ----------------
            purchase_item = await repo_purchase_item.create(
                PurchaseItem(
                    product_id=product.id,
                    purchase_id=purchase.id,
                    quantity=100,
                    unit_price=Decimal("10000")
                )
            )

            # ---------------- DOCUMENT ----------------
            document = await repo_document.create(
                Document(
                    file_url="/docs/ticket_001.pdf",
                    filename="ticket_compra_001",
                    purchase_id=purchase.id
                )
            )

            # ---------------- STOCK MOVEMENT ----------------
            await repo_stock.create(
                StockMovement(
                    product_id=product.id,
                    reference_id=purchase.id,
                    quantity=100,
                    movement_type=StockMovementType.IN,
                    reference_type=StockMovementReferenceType.PURCHASE
                )
            )

            await db.commit()

            print("Seed Execute OK")

        except Exception as e:
            await db.rollback()
            raise e


if __name__ == "__main__":
    asyncio.run(seed())