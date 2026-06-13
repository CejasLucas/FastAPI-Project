import asyncio
from app.infrastructure.database.session import SessionLocal

from app.infrastructure.repositories.brand_repository import SqlAlchemyBrandRepository
from app.infrastructure.repositories.supplier_repository import SqlAlchemySupplierRepository
from app.infrastructure.repositories.category_repository import SqlAlchemyCategoryRepository
from app.infrastructure.repositories.product_repository import SqlAlchemyProductRepository
from app.infrastructure.repositories.purchase_repository import SqlAlchemyPurchaseRepository
from app.infrastructure.repositories.purchase_item_repository import SqlAlchemyPurchaseItemRepository
from app.infrastructure.repositories.document_repository import SqlAlchemyDocumentRepository
from app.infrastructure.repositories.stock_movement_repository import SqlAlchemyStockMovementRepository

from app.scripts.seeders.brand_seeder import build_brands
from app.scripts.seeders.supplier_seeder import build_suppliers
from app.scripts.seeders.category_seeder import build_categories
from app.scripts.seeders.product_seeder import build_products
from app.scripts.seeders.purchase_seeder import build_purchases
from app.scripts.seeders.purchase_item_seeder import build_purchase_items
from app.scripts.seeders.document_seeder import build_documents
from app.scripts.seeders.stock_movement_seeder import build_stock_movements


async def persist_entities(entities, create_fn):
    return [await create_fn(e) for e in entities]


def calculate_purchase_total(items):
    return sum(item.quantity * item.unit_price for item in items)


async def seed():
    async with SessionLocal() as db:

        brand_repo = SqlAlchemyBrandRepository(db)
        supplier_repo = SqlAlchemySupplierRepository(db)
        category_repo = SqlAlchemyCategoryRepository(db)
        product_repo = SqlAlchemyProductRepository(db)
        purchase_repo = SqlAlchemyPurchaseRepository(db)
        purchase_item_repo = SqlAlchemyPurchaseItemRepository(db)
        document_repo = SqlAlchemyDocumentRepository(db)
        stock_repo = SqlAlchemyStockMovementRepository(db)

        try:
            print("Seeding suppliers...")
            suppliers = await persist_entities(build_suppliers(), supplier_repo.create)
            supplier_map = {s.name: s for s in suppliers}
            print(f"{len(suppliers)} suppliers created")

            print("Seeding brands...")
            brands = await persist_entities(build_brands(), brand_repo.create)
            brand_map = {b.name: b for b in brands}
            print(f"{len(brands)} brands created")

            print("Seeding categories...")
            categories = await persist_entities(build_categories(), category_repo.create)
            category_map = {c.name: c for c in categories}
            print(f"{len(categories)} categories created")


            print("Seeding products...")
            products = await persist_entities(
                build_products(category_map, brand_map),
                product_repo.create
            )
            product_map = {p.sku: p for p in products}
            print(f"{len(products)} products created")


            print("Seeding purchases...")
            purchases = await persist_entities(
                build_purchases(supplier_map),
                purchase_repo.create
            )
            print(f"{len(purchases)} purchases created")


            print("Seeding purchase items...")
            purchase_items = await persist_entities(
                build_purchase_items(purchases, product_map),
                purchase_item_repo.create
            )
            print(f"{len(purchase_items)} purchase items created")


            print("Recalculating purchase totals...")
            for purchase in purchases:
                items = [i for i in purchase_items if i.purchase_id == purchase.id]
                purchase.total_amount = calculate_purchase_total(items)
                await purchase_repo.update(purchase)


            print("Creating stock movements...")
            stock_movements = await persist_entities(
                build_stock_movements(purchase_items),
                stock_repo.create
            )
            print(f"{len(stock_movements)} stock movements created")


            print("Creating documents...")
            documents = await persist_entities(
                build_documents(purchases),
                document_repo.create
            )
            print(f"{len(documents)} documents created")


            await db.commit()
            print("Seed executed successfully 🚀")

        except Exception as ex:
            await db.rollback()
            print(f"Seed error: {ex}")
            raise


if __name__ == "__main__":
    asyncio.run(seed())