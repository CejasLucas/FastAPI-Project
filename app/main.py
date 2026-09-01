from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.database.base import Base
from app.infrastructure.database.session import engine

from app.api.routes.api_health import router as api_health_router
from app.api.routes.supplier_routes import router as supplier_router
from app.api.routes.brand_routes import router as brand_router
from app.api.routes.category_routes import router as category_router
from app.api.routes.product_routes import router as product_router
from app.api.routes.purchase_routes import router as purchase_router
from app.api.routes.purchase_item_routes import router as purchase_item_router
from app.api.routes.dashboard_routes import router as dashboard_router

app = FastAPI(title="AutoParts API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://192.168.0.12:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_health_router)
app.include_router(supplier_router)
app.include_router(brand_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(purchase_router)
app.include_router(purchase_item_router)
app.include_router(dashboard_router)

@app.on_event("startup")
async def startup():
    print("🏁 Tables registry:", Base.metadata.tables.keys())
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
async def health():
    return {"status": "ok"}