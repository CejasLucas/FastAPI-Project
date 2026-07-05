import calendar

from app.api.dtos.dashboard_dto import (
    DashboardSummaryDTO,
    DashboardCountsDTO,
    ExpensesPerMonthDTO,
    CategorySpendingDTO,
    SupplierSpendingDTO,
    RecentPurchaseDTO,
    LowStockProductDTO,
)
from app.domain.enums.purchase_status import PurchaseStatus

MONTH_FIELDS = [calendar.month_abbr[i].lower() for i in range(1, 13)]


def _status_value(status) -> str:
    """Normaliza el status a string, sea Enum o str plano."""
    return status.value if hasattr(status, "value") else status


class DashboardService:
    def __init__(self, supplier_repo, product_repo, purchase_repo):
        self.supplier_repository = supplier_repo
        self.product_repository = product_repo
        self.purchase_repository = purchase_repo

    async def get_summary(self, year: int = 2026) -> DashboardSummaryDTO:
        counts = await self.get_counts(year)
        expenses_per_month = await self.get_expenses_per_month(year)
        spending_by_category = await self.get_spending_by_category(year)
        top_suppliers = await self.get_top_suppliers(year)
        recent_purchases = await self.get_recent_purchases()
        low_stock_products = await self.get_low_stock_products()

        return DashboardSummaryDTO(
            year=year,
            counts=counts,
            expenses_per_month=expenses_per_month,
            spending_by_category=spending_by_category,
            top_suppliers=top_suppliers,
            recent_purchases=recent_purchases,
            low_stock_products=low_stock_products,
        )

    async def get_counts(self, year: int = 2026) -> DashboardCountsDTO:
        purchases_count = await self.purchase_repository.count_by_year(year)
        products_count = await self.product_repository.count_all()
        suppliers_count = await self.supplier_repository.count_all()
        low_stock = await self.product_repository.get_low_stock(limit=1000)

        total_pending = await self.purchase_repository.get_total_by_status_and_year(
            year, PurchaseStatus.PENDING
        )

        return DashboardCountsDTO(
            amount_purchases=purchases_count,
            amount_products=products_count,
            amount_suppliers=suppliers_count,
            low_stock_count=len(low_stock),
            total_pending=total_pending,
        )

    async def get_expenses_per_month(self, year: int = 2026) -> ExpensesPerMonthDTO:
        purchases = await self.purchase_repository.get_purchases_by_year(year)

        totals = {month: 0.0 for month in MONTH_FIELDS}
        for purchase in purchases:
            month_key = MONTH_FIELDS[purchase.purchase_date.month - 1]
            totals[month_key] += float(purchase.total_amount)

        return ExpensesPerMonthDTO(**totals)

    async def get_total_spent(self, year: int = 2026) -> float:
        purchases = await self.purchase_repository.get_purchases_by_year(year)
        return sum(float(p.total_amount) for p in purchases)

    async def get_spending_by_category(self, year: int = 2026, limit: int = 5) -> list[CategorySpendingDTO]:
        purchases = await self.purchase_repository.get_purchases_by_year(year)

        totals: dict[str, float] = {}
        for purchase in purchases:
            for item in purchase.items:
                category_name = item.product.category.name if item.product.category else "Sin categoría"
                subtotal = float(item.quantity) * float(item.unit_price)
                totals[category_name] = totals.get(category_name, 0.0) + subtotal

        sorted_items = sorted(totals.items(), key=lambda x: x[1], reverse=True)[:limit]
        return [CategorySpendingDTO(category=cat, total=total) for cat, total in sorted_items]

    async def get_top_suppliers(self, year: int = 2026, limit: int = 5) -> list[SupplierSpendingDTO]:
        purchases = await self.purchase_repository.get_purchases_by_year(year)

        totals: dict[str, float] = {}
        for purchase in purchases:
            if not purchase.supplier:
                continue
            supplier_name = purchase.supplier.name
            totals[supplier_name] = totals.get(supplier_name, 0.0) + float(purchase.total_amount)

        sorted_items = sorted(totals.items(), key=lambda x: x[1], reverse=True)[:limit]
        return [SupplierSpendingDTO(supplier=name, total=total) for name, total in sorted_items]

    async def get_recent_purchases(self, limit: int = 12) -> list[RecentPurchaseDTO]:
        purchases = await self.purchase_repository.get_recent(limit=limit)

        return [
            RecentPurchaseDTO(
                id=p.id,
                supplier=p.supplier.name if p.supplier else "Sin proveedor",
                purchase_date=p.purchase_date,
                status=_status_value(p.status),
                total_amount=float(p.total_amount),
            )
            for p in purchases
        ]

    async def get_low_stock_products(self, limit: int = 10) -> list[LowStockProductDTO]:
        products = await self.product_repository.get_low_stock(limit=limit)

        return [
            LowStockProductDTO(
                id=prod.id,
                name=prod.name,
                current_stock=prod.current_stock,
                minimum_stock=prod.minimum_stock,
            )
            for prod in products
        ]