from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/users/", UserListView.as_view(), name="user-list"),
    path("api/users/create/", UserCreateView.as_view(), name="user-create"),
    path("api/users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("api/users/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("api/users/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("api/tags/", TagListView.as_view(), name="tag-list"),
    path("api/tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("api/tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
    path("api/tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("api/tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path(
        "api/income-categories/",
        IncomeCategoryListView.as_view(),
        name="income-category-list",
    ),
    path(
        "api/income-categories/create/",
        IncomeCategoryCreateView.as_view(),
        name="income-category-create",
    ),
    path(
        "api/income-categories/<int:pk>/",
        IncomeCategoryDetailView.as_view(),
        name="income-category-detail",
    ),
    path(
        "api/income-categories/<int:pk>/update/",
        IncomeCategoryUpdateView.as_view(),
        name="income-category-update",
    ),
    path(
        "api/income-categories/<int:pk>/delete/",
        IncomeCategoryDeleteView.as_view(),
        name="income-category-delete",
    ),
    path(
        "api/expense-categories/",
        ExpenseCategoryListView.as_view(),
        name="expense-category-list",
    ),
    path(
        "api/expense-categories/create/",
        ExpenseCategoryCreateView.as_view(),
        name="expense-category-create",
    ),
    path(
        "api/expense-categories/<int:pk>/",
        ExpenseCategoryDetailView.as_view(),
        name="expense-category-detail",
    ),
    path(
        "api/expense-categories/<int:pk>/update/",
        ExpenseCategoryUpdateView.as_view(),
        name="expense-category-update",
    ),
    path(
        "api/expense-categories/<int:pk>/delete/",
        ExpenseCategoryDeleteView.as_view(),
        name="expense-category-delete",
    ),
    path(
        "api/financial-sources/",
        FinancialSourceListView.as_view(),
        name="financial-source-list",
    ),
    path(
        "api/financial-sources/create/",
        FinancialSourceCreateView.as_view(),
        name="financial-source-create",
    ),
    path(
        "api/financial-sources/<int:pk>/",
        FinancialSourceDetailView.as_view(),
        name="financial-source-detail",
    ),
    path(
        "api/financial-sources/<int:pk>/update/",
        FinancialSourceUpdateView.as_view(),
        name="financial-source-update",
    ),
    path(
        "api/financial-sources/<int:pk>/delete/",
        FinancialSourceDeleteView.as_view(),
        name="financial-source-delete",
    ),
    path("api/income-plans/", IncomePlanListView.as_view(), name="income-plan-list"),
    path(
        "api/income-plans/create/",
        IncomePlanCreateView.as_view(),
        name="income-plan-create",
    ),
    path(
        "api/income-plans/<int:pk>/",
        IncomePlanDetailView.as_view(),
        name="income-plan-detail",
    ),
    path(
        "api/income-plans/<int:pk>/update/",
        IncomePlanUpdateView.as_view(),
        name="income-plan-update",
    ),
    path(
        "api/income-plans/<int:pk>/delete/",
        IncomePlanDeleteView.as_view(),
        name="income-plan-delete",
    ),
    path("api/incomes/", IncomeListView.as_view(), name="income-list"),
    path("api/incomes/create/", IncomeCreateView.as_view(), name="income-create"),
    path("api/incomes/<int:pk>/", IncomeDetailView.as_view(), name="income-detail"),
    path(
        "api/incomes/<int:pk>/update/", IncomeUpdateView.as_view(), name="income-update"
    ),
    path(
        "api/incomes/<int:pk>/delete/", IncomeDeleteView.as_view(), name="income-delete"
    ),
    path("api/expense-plans/", ExpensePlanListView.as_view(), name="expense-plan-list"),
    path(
        "api/expense-plans/create/",
        ExpensePlanCreateView.as_view(),
        name="expense-plan-create",
    ),
    path(
        "api/expense-plans/<int:pk>/",
        ExpensePlanDetailView.as_view(),
        name="expense-plan-detail",
    ),
    path(
        "api/expense-plans/<int:pk>/update/",
        ExpensePlanUpdateView.as_view(),
        name="expense-plan-update",
    ),
    path(
        "api/expense-plans/<int:pk>/delete/",
        ExpensePlanDeleteView.as_view(),
        name="expense-plan-delete",
    ),
    path("api/expenses/", ExpenseListView.as_view(), name="expense-list"),
    path("api/expenses/create/", ExpenseCreateView.as_view(), name="expense-create"),
    path("api/expenses/<int:pk>/", ExpenseDetailView.as_view(), name="expense-detail"),
    path(
        "api/expenses/<int:pk>/update/",
        ExpenseUpdateView.as_view(),
        name="expense-update",
    ),
    path(
        "api/expenses/<int:pk>/delete/",
        ExpenseDeleteView.as_view(),
        name="expense-delete",
    ),
    path("api/investments/", InvestmentListView.as_view(), name="investment-list"),
    path(
        "api/investments/create/",
        InvestmentCreateView.as_view(),
        name="investment-create",
    ),
    path(
        "api/investments/<int:pk>/",
        InvestmentDetailView.as_view(),
        name="investment-detail",
    ),
    path(
        "api/investments/<int:pk>/update/",
        InvestmentUpdateView.as_view(),
        name="investment-update",
    ),
    path(
        "api/investments/<int:pk>/delete/",
        InvestmentDeleteView.as_view(),
        name="investment-delete",
    ),
    path(
        "api/investment-plans/",
        InvestmentPlanListView.as_view(),
        name="investment-plan-list",
    ),
    path(
        "api/investment-plans/create/",
        InvestmentPlanCreateView.as_view(),
        name="investment-plan-create",
    ),
    path(
        "api/investment-plans/<int:pk>/",
        InvestmentPlanDetailView.as_view(),
        name="investment-plan-detail",
    ),
    path(
        "api/investment-plans/<int:pk>/update/",
        InvestmentPlanUpdateView.as_view(),
        name="investment-plan-update",
    ),
    path(
        "api/investment-plans/<int:pk>/delete/",
        InvestmentPlanDeleteView.as_view(),
        name="investment-plan-delete",
    ),
    path("api/debts/", DebtListView.as_view(), name="debt-list"),
    path("api/debts/create/", DebtCreateView.as_view(), name="debt-create"),
    path("api/debts/<int:pk>/", DebtDetailView.as_view(), name="debt-detail"),
    path("api/debts/<int:pk>/update/", DebtUpdateView.as_view(), name="debt-update"),
    path("api/debts/<int:pk>/delete/", DebtDeleteView.as_view(), name="debt-delete"),
    path("api/debt-plans/", DebtPlanListView.as_view(), name="debt-plan-list"),
    path(
        "api/debt-plans/create/", DebtPlanCreateView.as_view(), name="debt-plan-create"
    ),
    path(
        "api/debt-plans/<int:pk>/",
        DebtPlanDetailView.as_view(),
        name="debt-plan-detail",
    ),
    path(
        "api/debt-plans/<int:pk>/update/",
        DebtPlanUpdateView.as_view(),
        name="debt-plan-update",
    ),
    path(
        "api/debt-plans/<int:pk>/delete/",
        DebtPlanDeleteView.as_view(),
        name="debt-plan-delete",
    ),
    path("api/claims/", ClaimListView.as_view(), name="claim-list"),
    path("api/claims/create/", ClaimCreateView.as_view(), name="claim-create"),
    path("api/claims/<int:pk>/", ClaimDetailView.as_view(), name="claim-detail"),
    path("api/claims/<int:pk>/update/", ClaimUpdateView.as_view(), name="claim-update"),
    path("api/claims/<int:pk>/delete/", ClaimDeleteView.as_view(), name="claim-delete"),
    path("api/claim-plans/", ClaimPlanListView.as_view(), name="claim-plan-list"),
    path(
        "api/claim-plans/create/",
        ClaimPlanCreateView.as_view(),
        name="claim-plan-create",
    ),
    path(
        "api/claim-plans/<int:pk>/",
        ClaimPlanDetailView.as_view(),
        name="claim-plan-detail",
    ),
    path(
        "api/claim-plans/<int:pk>/update/",
        ClaimPlanUpdateView.as_view(),
        name="claim-plan-update",
    ),
    path(
        "api/claim-plans/<int:pk>/delete/",
        ClaimPlanDeleteView.as_view(),
        name="claim-plan-delete",
    ),
    path("api/bank-accounts/", BankAccountListView.as_view(), name="bank-account-list"),
    path(
        "api/bank-accounts/create/",
        BankAccountCreateView.as_view(),
        name="bank-account-create",
    ),
    path(
        "api/bank-accounts/<int:pk>/",
        BankAccountDetailView.as_view(),
        name="bank-account-detail",
    ),
    path(
        "api/bank-accounts/<int:pk>/update/",
        BankAccountUpdateView.as_view(),
        name="bank-account-update",
    ),
    path(
        "api/bank-accounts/<int:pk>/delete/",
        BankAccountDeleteView.as_view(),
        name="bank-account-delete",
    ),
    path("api/transactions/", TransactionListView.as_view(), name="transaction-list"),
    path(
        "api/transactions/create/",
        TransactionCreateView.as_view(),
        name="transaction-create",
    ),
    path(
        "api/transactions/<int:pk>/",
        TransactionDetailView.as_view(),
        name="transaction-detail",
    ),
    path(
        "api/transactions/<int:pk>/update/",
        TransactionUpdateView.as_view(),
        name="transaction-update",
    ),
    path(
        "api/transactions/<int:pk>/delete/",
        TransactionDeleteView.as_view(),
        name="transaction-delete",
    ),
]
