from datetime import date
from uuid import UUID

from pydantic import BaseModel

# =========================
# COUNTS
# =========================
class DashboardCountsDTO(BaseModel):
    amount_purchases: int
    amount_products: int
    amount_suppliers: int
    low_stock_count: int
    total_spent: float


# =========================
# KPI
# =========================
class DashboardKPIDTO(BaseModel):
    average_purchase: float
    largest_purchase: float
    purchases_this_month: int
    spending_this_month: float
    monthly_growth_percentage: float


# =========================
# CHARTS
# =========================
class MonthlyExpenseDTO(BaseModel):
    month: str
    total: float

class CategorySpendingDTO(BaseModel):
    category: str
    total: float

class SupplierSpendingDTO(BaseModel):
    supplier: str
    total: float

class TopProductDTO(BaseModel):
    product: str
    quantity: int


# =========================
# TABLES
# =========================
class RecentPurchaseDTO(BaseModel):
    id: UUID
    supplier: str
    purchase_date: date
    status: str
    total_amount: float


class LowStockProductDTO(BaseModel):
    id: UUID
    name: str
    current_stock: int
    minimum_stock: int
    missing_stock: int


# =========================
# RESPONSE PRINCIPAL
# =========================
class DashboardSummaryDTO(BaseModel):
    year: int
    counts: DashboardCountsDTO
    kpis: DashboardKPIDTO
    monthly_expenses: list[MonthlyExpenseDTO]
    spending_by_category: list[CategorySpendingDTO]
    top_suppliers: list[SupplierSpendingDTO]
    top_products: list[TopProductDTO]
    recent_purchases: list[RecentPurchaseDTO]
    low_stock_products: list[LowStockProductDTO]
