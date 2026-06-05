from fastapi import FastAPI

from app.infrastructure.database.base import Base
from app.infrastructure.database.session import engine

from app.api.routes.supplier_routes import router as supplier_router
from app.api.routes.category_routes import router as category_router
from app.api.routes.product_routes import router as product_router
from app.api.routes.document_routes import router as document_router
from app.api.routes.purchase_routes import router as purchase_router
from app.api.routes.purchase_item_routes import router as purchase_item_router
from app.api.routes.stock_movement_routes import router as stock_movement_router

app = FastAPI(title="AutoParts API")

app.include_router(supplier_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(document_router)
app.include_router(purchase_router)
app.include_router(purchase_item_router)
app.include_router(stock_movement_router)

@app.on_event("startup")
async def startup():
    print("🏁 Tables registry:", Base.metadata.tables.keys())
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
async def health():
    return {"status": "ok"}