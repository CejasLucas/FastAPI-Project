from datetime import datetime
from app.api.dtos.dashboard_dto import (
    DashboardSummaryDTO,
    DashboardCountsDTO,
    DashboardKPIDTO,
    MonthlyExpenseDTO,
    CategorySpendingDTO,
    SupplierSpendingDTO,
    TopProductDTO,
    RecentPurchaseDTO,
    LowStockProductDTO,
)


def _status_value(status)->str:
    return status.value if hasattr(status,"value") else status


class DashboardService:

    def __init__(self,supplier_repo,product_repo,purchase_repo):
        self.supplier_repository=supplier_repo
        self.product_repository=product_repo
        self.purchase_repository=purchase_repo


    async def get_summary(self,year:int=2026)->DashboardSummaryDTO:

        purchases=await self.purchase_repository.get_confirmed_by_year(year)

        return DashboardSummaryDTO(
            year=year,
            counts=await self.get_counts(purchases),
            kpis=await self.get_kpis(purchases),
            monthly_expenses=self.get_monthly_expenses(purchases),
            spending_by_category=self.get_spending_by_category(purchases),
            top_suppliers=self.get_top_suppliers(purchases),
            top_products=self.get_top_products(purchases),
            recent_purchases=await self.get_recent_purchases(),
            low_stock_products=await self.get_low_stock_products()
        )


    async def get_counts(self,purchases):

        low_stock=await self.product_repository.get_low_stock(limit=100)


        return DashboardCountsDTO(
            amount_purchases=len(purchases),
            amount_products=await self.product_repository.count_all(),
            amount_suppliers=await self.supplier_repository.count_all(),
            low_stock_count=len(low_stock),
            total_spent=sum(float(p.total_amount) for p in purchases)
        )


    async def get_kpis(self,purchases):

        if not purchases:
            return DashboardKPIDTO(
                average_purchase=0,
                largest_purchase=0,
                purchases_this_month=0,
                spending_this_month=0,
                monthly_growth_percentage=0
            )


        amounts=[
            float(p.total_amount)
            for p in purchases
        ]


        now=datetime.now()


        current=[
            p for p in purchases
            if p.purchase_date.month==now.month
        ]


        previous=[
            p for p in purchases
            if p.purchase_date.month==now.month-1
        ]


        current_total=sum(
            float(p.total_amount)
            for p in current
        )


        previous_total=sum(
            float(p.total_amount)
            for p in previous
        )


        growth=0

        if previous_total>0:
            growth=((current_total-previous_total)/previous_total)*100


        return DashboardKPIDTO(
            average_purchase=sum(amounts)/len(amounts),
            largest_purchase=max(amounts),
            purchases_this_month=len(current),
            spending_this_month=current_total,
            monthly_growth_percentage=growth
        )


    def get_monthly_expenses(self,purchases):

        months={}


        for purchase in purchases:

            month=purchase.purchase_date.month

            months[month]=(
                months.get(month,0)
                +
                float(purchase.total_amount)
            )


        return [
            MonthlyExpenseDTO(
                month=datetime(2026,month,1).strftime("%b"),
                total=total
            )
            for month,total in sorted(months.items())
        ]


    def get_spending_by_category(self,purchases,limit=5):

        totals={}


        for purchase in purchases:

            for item in purchase.items:

                category=(
                    item.product.category.name
                    if item.product.category
                    else "Sin categoría"
                )

                subtotal=float(item.quantity)*float(item.unit_price)

                totals[category]=(
                    totals.get(category,0)
                    +
                    subtotal
                )


        result=sorted(
            totals.items(),
            key=lambda x:x[1],
            reverse=True
        )[:limit]


        return [
            CategorySpendingDTO(
                category=name,
                total=value
            )
            for name,value in result
        ]


    def get_top_suppliers(self,purchases,limit=5):

        totals={}


        for purchase in purchases:

            if not purchase.supplier:
                continue

            name=purchase.supplier.name

            totals[name]=(
                totals.get(name,0)
                +
                float(purchase.total_amount)
            )


        result=sorted(
            totals.items(),
            key=lambda x:x[1],
            reverse=True
        )[:limit]


        return [
            SupplierSpendingDTO(
                supplier=name,
                total=value
            )
            for name,value in result
        ]


    def get_top_products(self,purchases,limit=5):

        products={}


        for purchase in purchases:

            for item in purchase.items:

                name=item.product.name

                products[name]=(
                    products.get(name,0)
                    +
                    int(item.quantity)
                )


        result=sorted(
            products.items(),
            key=lambda x:x[1],
            reverse=True
        )[:limit]


        return [
            TopProductDTO(
                product=name,
                quantity=value
            )
            for name,value in result
        ]


    async def get_recent_purchases(self,limit=12):

        purchases=await self.purchase_repository.get_recent(limit)


        return [
            RecentPurchaseDTO(
                id=p.id,
                supplier=p.supplier.name if p.supplier else "Sin proveedor",
                purchase_date=p.purchase_date,
                status=_status_value(p.status),
                total_amount=float(p.total_amount)
            )
            for p in purchases
        ]


    async def get_low_stock_products(self,limit=10):

        products=await self.product_repository.get_low_stock(limit)


        return [
            LowStockProductDTO(
                id=p.id,
                name=p.name,
                current_stock=p.current_stock,
                minimum_stock=p.minimum_stock,
                missing_stock=max(
                    p.minimum_stock-p.current_stock,
                    0
                )
            )
            for p in products
        ]