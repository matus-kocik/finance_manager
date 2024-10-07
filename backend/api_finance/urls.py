from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/users/", UserListView.as_view(), name="user_list"),
    path("api/users/create/", UserCreateView.as_view(), name="user_create"),
    path(
        "api/users/<int:pk>/", UserDetailUpdateDeleteView.as_view(), name="user_detail"
    ),
    path("api/tags/", TagListView.as_view(), name="tag_list"),
    path("api/tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("api/tags/<int:pk>/", TagDetailUpdateDeleteView.as_view(), name="tag_detail"),
    path(
        "api/income-categories/",
        IncomeCategoryListView.as_view(),
        name="income_category_list",
    ),
    path(
        "api/income-categories/create/",
        IncomeCategoryCreateView.as_view(),
        name="income_category_create",
    ),
    path(
        "api/income-categories/<int:pk>/",
        IncomeCategoryDetailUpdateDeleteView.as_view(),
        name="income_category_detail",
    ),
    path(
        "api/expense-categories/",
        ExpenseCategoryListView.as_view(),
        name="expense_category_list",
    ),
    path(
        "api/expense-categories/create/",
        ExpenseCategoryCreateView.as_view(),
        name="expense_category_create",
    ),
    path(
        "api/expense-categories/<int:pk>/",
        ExpenseCategoryDetailUpdateDeleteView.as_view(),
        name="expense_category_detail",
    ),
    path(
        "api/financial-sources/",
        FinancialSourceListView.as_view(),
        name="financial_source_list",
    ),
    path(
        "api/financial-sources/create/",
        FinancialSourceCreateView.as_view(),
        name="financial_source_create",
    ),
    path(
        "api/financial-sources/<int:pk>/",
        FinancialSourceDetailUpdateDeleteView.as_view(),
        name="financial_source_detail",
    ),
    path("api/income-plans/", IncomePlanListView.as_view(), name="income_plan_list"),
    path(
        "api/income-plans/create/",
        IncomePlanCreateView.as_view(),
        name="income_plan_create",
    ),
    path(
        "api/income-plans/<int:pk>/",
        IncomePlanDetailUpdateDeleteView.as_view(),
        name="income_plan_detail",
    ),
    path("api/incomes/", IncomeListView.as_view(), name="income_list"),
    path("api/incomes/create/", IncomeCreateView.as_view(), name="income_create"),
    path(
        "api/incomes/<int:pk>/",
        IncomeDetailUpdateDeleteView.as_view(),
        name="income_detail",
    ),
    path("api/expense-plans/", ExpensePlanListView.as_view(), name="expense_plan_list"),
    path(
        "api/expense-plans/create/",
        ExpensePlanCreateView.as_view(),
        name="expense_plan_create",
    ),
    path(
        "api/expense-plans/<int:pk>/",
        ExpensePlanDetailUpdateDeleteView.as_view(),
        name="expense_plan_detail",
    ),
    path("api/expenses/", ExpenseListView.as_view(), name="expense_list"),
    path("api/expenses/create/", ExpenseCreateView.as_view(), name="expense_create"),
    path(
        "api/expenses/<int:pk>/",
        ExpenseDetailUpdateDeleteView.as_view(),
        name="expense_detail",
    ),
    path("api/investments/", InvestmentListView.as_view(), name="investment_list"),
    path(
        "api/investments/create/",
        InvestmentCreateView.as_view(),
        name="investment_create",
    ),
    path(
        "api/investments/<int:pk>/",
        InvestmentDetailUpdateDeleteView.as_view(),
        name="investment_detail",
    ),
    path(
        "api/investment-plans/",
        InvestmentPlanListView.as_view(),
        name="investment_plan_list",
    ),
    path(
        "api/investment-plans/create/",
        InvestmentPlanCreateView.as_view(),
        name="investment_plan_create",
    ),
    path(
        "api/investment-plans/<int:pk>/",
        InvestmentPlanDetailUpdateDeleteView.as_view(),
        name="investment_plan_detail",
    ),
    path("api/debts/", DebtListView.as_view(), name="debt_list"),
    path("api/debts/create/", DebtCreateView.as_view(), name="debt_create"),
    path(
        "api/debts/<int:pk>/", DebtDetailUpdateDeleteView.as_view(), name="debt_detail"
    ),
    path("api/debt-plans/", DebtPlanListView.as_view(), name="debt_plan_list"),
    path(
        "api/debt-plans/create/", DebtPlanCreateView.as_view(), name="debt_plan_create"
    ),
    path(
        "api/debt-plans/<int:pk>/",
        DebtPlanDetailUpdateDeleteView.as_view(),
        name="debt_plan_detail",
    ),
    path("api/claims/", ClaimListView.as_view(), name="claim_list"),
    path("api/claims/create/", ClaimCreateView.as_view(), name="claim_create"),
    path(
        "api/claims/<int:pk>/",
        ClaimDetailUpdateDeleteView.as_view(),
        name="claim_detail",
    ),
    path("api/claim-plans/", ClaimPlanListView.as_view(), name="claim_plan_list"),
    path(
        "api/claim-plans/create/",
        ClaimPlanCreateView.as_view(),
        name="claim_plan_create",
    ),
    path(
        "api/claim-plans/<int:pk>/",
        ClaimPlanDetailUpdateDeleteView.as_view(),
        name="claim_plan_detail",
    ),
    path("api/bank-accounts/", BankAccountListView.as_view(), name="bank_account_list"),
    path(
        "api/bank-accounts/create/",
        BankAccountCreateView.as_view(),
        name="bank_account_create",
    ),
    path(
        "api/bank-accounts/<int:pk>/",
        BankAccountDetailUpdateDeleteView.as_view(),
        name="bank_account_detail",
    ),
    path("api/transactions/", TransactionListView.as_view(), name="transaction_list"),
    path(
        "api/transactions/create/",
        TransactionCreateView.as_view(),
        name="transaction_create",
    ),
    path(
        "api/transactions/<int:pk>/",
        TransactionDetailUpdateDeleteView.as_view(),
        name="transaction_detail",
    ),
]
