from django.contrib import admin
from .models import (
    Tag,
    IncomeCategory,
    ExpenseCategory,
    FinancialSource,
    IncomePlan,
    Income,
    ExpensePlan,
    Expense,
    InvestmentPlan,
    Investment,
    DebtPlan,
    Debt,
    ClaimPlan,
    Claim,
    BankAccount,
    Transaction,
)

# Register your models here.
admin.site.register(Tag)
admin.site.register(IncomeCategory)
admin.site.register(ExpenseCategory)
admin.site.register(FinancialSource)
admin.site.register(IncomePlan)
admin.site.register(Income)
admin.site.register(ExpensePlan)
admin.site.register(Expense)
admin.site.register(InvestmentPlan)
admin.site.register(Investment)
admin.site.register(DebtPlan)
admin.site.register(Debt)
admin.site.register(ClaimPlan)
admin.site.register(Claim)
admin.site.register(BankAccount)
admin.site.register(Transaction)
