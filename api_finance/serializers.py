from rest_framework import serializers
from django.contrib.auth.models import User
from finance.models import (
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class BaseModelSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        abstract = True


class IncomeCategorySerializer(BaseModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = "__all__"


class ExpenseCategorySerializer(BaseModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = "__all__"


class FinancialSourceSerializer(BaseModelSerializer):
    class Meta:
        model = FinancialSource
        fields = "__all__"


class IncomePlanSerializer(BaseModelSerializer):
    source = FinancialSourceSerializer()
    category = IncomeCategorySerializer()

    class Meta:
        model = IncomePlan
        fields = "__all__"


class IncomeSerializer(BaseModelSerializer):
    source = FinancialSourceSerializer()
    category = IncomeCategorySerializer()

    class Meta:
        model = Income
        fields = "__all__"


class ExpensePlanSerializer(BaseModelSerializer):
    source = FinancialSourceSerializer()
    category = ExpenseCategorySerializer()

    class Meta:
        model = ExpensePlan
        fields = "__all__"


class ExpenseSerializer(BaseModelSerializer):
    source = FinancialSourceSerializer()
    category = ExpenseCategorySerializer()

    class Meta:
        model = Expense
        fields = "__all__"


class InvestmentPlanSerializer(ExpensePlanSerializer):
    class Meta:
        model = InvestmentPlan
        fields = "__all__"


class InvestmentSerializer(ExpenseSerializer):
    class Meta:
        model = Investment
        fields = "__all__"


class DebtPlanSerializer(ExpensePlanSerializer):
    class Meta:
        model = DebtPlan
        fields = "__all__"


class DebtSerializer(ExpenseSerializer):
    class Meta:
        model = Debt
        fields = "__all__"


class ClaimPlanSerializer(IncomePlanSerializer):
    class Meta:
        model = ClaimPlan
        fields = "__all__"


class ClaimSerializer(IncomeSerializer):
    class Meta:
        model = Claim
        fields = "__all__"


class BankAccountSerializer(BaseModelSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"


class TransactionSerializer(BaseModelSerializer):
    bank_account = BankAccountSerializer()
    related_income = IncomeSerializer()
    related_expense = ExpenseSerializer()

    class Meta:
        model = Transaction
        fields = "__all__"
