from datetime import date
from uuid import UUID
from pydantic import BaseModel


class ExpensesPerMonthDTO(BaseModel):
    jan: float = 0; feb: float = 0; mar: float = 0; apr: float = 0
    may: float = 0; jun: float = 0; jul: float = 0; aug: float = 0
    sep: float = 0; oct: float = 0; nov: float = 0; dec: float = 0


class CategorySpendingDTO(BaseModel):
    category: str
    total: float


class SupplierSpendingDTO(BaseModel):
    supplier: str
    total: float


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


class DashboardCountsDTO(BaseModel):
    amount_purchases: int
    amount_products: int
    amount_suppliers: int
    low_stock_count: int
    total_pending: float


class DashboardSummaryDTO(BaseModel):
    year: int
    counts: DashboardCountsDTO
    expenses_per_month: ExpensesPerMonthDTO
    spending_by_category: list[CategorySpendingDTO]
    top_suppliers: list[SupplierSpendingDTO]
    recent_purchases: list[RecentPurchaseDTO]
    low_stock_products: list[LowStockProductDTO]