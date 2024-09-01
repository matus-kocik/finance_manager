from rest_framework import generics
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
    Investment,
    InvestmentPlan,
    Debt,
    DebtPlan,
    Claim,
    ClaimPlan,
    BankAccount,
    Transaction,
)
from .serializers import (
    TagSerializer,
    UserSerializer,
    IncomeCategorySerializer,
    ExpenseCategorySerializer,
    FinancialSourceSerializer,
    IncomeSerializer,
    IncomePlanSerializer,
    ExpenseSerializer,
    ExpensePlanSerializer,
    InvestmentSerializer,
    InvestmentPlanSerializer,
    DebtSerializer,
    DebtPlanSerializer,
    ClaimSerializer,
    ClaimPlanSerializer,
    BankAccountSerializer,
    TransactionSerializer,
)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDeleteView(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IncomeCategoryListView(generics.ListAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer


class IncomeCategoryCreateView(generics.CreateAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer


class IncomeCategoryDetailView(generics.RetrieveAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer


class IncomeCategoryUpdateView(generics.UpdateAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer


class IncomeCategoryDeleteView(generics.DestroyAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer


class ExpenseCategoryListView(generics.ListAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class ExpenseCategoryCreateView(generics.CreateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class ExpenseCategoryDetailView(generics.RetrieveAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class ExpenseCategoryUpdateView(generics.UpdateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class ExpenseCategoryDeleteView(generics.DestroyAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class FinancialSourceListView(generics.ListAPIView):
    queryset = FinancialSource.objects.all()
    serializer_class = FinancialSourceSerializer


class FinancialSourceCreateView(generics.CreateAPIView):
    queryset = FinancialSource.objects.all()
    serializer_class = FinancialSourceSerializer


class FinancialSourceDetailView(generics.RetrieveAPIView):
    queryset = FinancialSource.objects.all()
    serializer_class = FinancialSourceSerializer


class FinancialSourceUpdateView(generics.UpdateAPIView):
    queryset = FinancialSource.objects.all()
    serializer_class = FinancialSourceSerializer


class FinancialSourceDeleteView(generics.DestroyAPIView):
    queryset = FinancialSource.objects.all()
    serializer_class = FinancialSourceSerializer


class IncomePlanListView(generics.ListAPIView):
    queryset = IncomePlan.objects.all()
    serializer_class = IncomePlanSerializer


class IncomePlanCreateView(generics.CreateAPIView):
    queryset = IncomePlan.objects.all()
    serializer_class = IncomePlanSerializer


class IncomePlanDetailView(generics.RetrieveAPIView):
    queryset = IncomePlan.objects.all()
    serializer_class = IncomePlanSerializer


class IncomePlanUpdateView(generics.UpdateAPIView):
    queryset = IncomePlan.objects.all()
    serializer_class = IncomePlanSerializer


class IncomePlanDeleteView(generics.DestroyAPIView):
    queryset = IncomePlan.objects.all()
    serializer_class = IncomePlanSerializer


class IncomeListView(generics.ListAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class IncomeCreateView(generics.CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class IncomeDetailView(generics.RetrieveAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class IncomeUpdateView(generics.UpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class IncomeDeleteView(generics.DestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class ExpensePlanListView(generics.ListAPIView):
    queryset = ExpensePlan.objects.all()
    serializer_class = ExpensePlanSerializer


class ExpensePlanCreateView(generics.CreateAPIView):
    queryset = ExpensePlan.objects.all()
    serializer_class = ExpensePlanSerializer


class ExpensePlanDetailView(generics.RetrieveAPIView):
    queryset = ExpensePlan.objects.all()
    serializer_class = ExpensePlanSerializer


class ExpensePlanUpdateView(generics.UpdateAPIView):
    queryset = ExpensePlan.objects.all()
    serializer_class = ExpensePlanSerializer


class ExpensePlanDeleteView(generics.DestroyAPIView):
    queryset = ExpensePlan.objects.all()
    serializer_class = ExpensePlanSerializer


class ExpenseListView(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseCreateView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetailView(generics.RetrieveAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseUpdateView(generics.UpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDeleteView(generics.DestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class InvestmentListView(generics.ListAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class InvestmentCreateView(generics.CreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class InvestmentDetailView(generics.RetrieveAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class InvestmentUpdateView(generics.UpdateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class InvestmentDeleteView(generics.DestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class InvestmentPlanListView(generics.ListAPIView):
    queryset = InvestmentPlan.objects.all()
    serializer_class = InvestmentPlanSerializer


class InvestmentPlanCreateView(generics.CreateAPIView):
    queryset = InvestmentPlan.objects.all()
    serializer_class = InvestmentPlanSerializer


class InvestmentPlanDetailView(generics.RetrieveAPIView):
    queryset = InvestmentPlan.objects.all()
    serializer_class = InvestmentPlanSerializer


class InvestmentPlanUpdateView(generics.UpdateAPIView):
    queryset = InvestmentPlan.objects.all()
    serializer_class = InvestmentPlanSerializer


class InvestmentPlanDeleteView(generics.DestroyAPIView):
    queryset = InvestmentPlan.objects.all()
    serializer_class = InvestmentPlanSerializer


class DebtListView(generics.ListAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class DebtCreateView(generics.CreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class DebtDetailView(generics.RetrieveAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class DebtUpdateView(generics.UpdateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class DebtDeleteView(generics.DestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class DebtPlanListView(generics.ListAPIView):
    queryset = DebtPlan.objects.all()
    serializer_class = DebtPlanSerializer


class DebtPlanCreateView(generics.CreateAPIView):
    queryset = DebtPlan.objects.all()
    serializer_class = DebtPlanSerializer


class DebtPlanDetailView(generics.RetrieveAPIView):
    queryset = DebtPlan.objects.all()
    serializer_class = DebtPlanSerializer


class DebtPlanUpdateView(generics.UpdateAPIView):
    queryset = DebtPlan.objects.all()
    serializer_class = DebtPlanSerializer


class DebtPlanDeleteView(generics.DestroyAPIView):
    queryset = DebtPlan.objects.all()
    serializer_class = DebtPlanSerializer


class ClaimListView(generics.ListAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ClaimCreateView(generics.CreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ClaimDetailView(generics.RetrieveAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ClaimUpdateView(generics.UpdateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ClaimDeleteView(generics.DestroyAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ClaimPlanListView(generics.ListAPIView):
    queryset = ClaimPlan.objects.all()
    serializer_class = ClaimPlanSerializer


class ClaimPlanCreateView(generics.CreateAPIView):
    queryset = ClaimPlan.objects.all()
    serializer_class = ClaimPlanSerializer


class ClaimPlanDetailView(generics.RetrieveAPIView):
    queryset = ClaimPlan.objects.all()
    serializer_class = ClaimPlanSerializer


class ClaimPlanUpdateView(generics.UpdateAPIView):
    queryset = ClaimPlan.objects.all()
    serializer_class = ClaimPlanSerializer


class ClaimPlanDeleteView(generics.DestroyAPIView):
    queryset = ClaimPlan.objects.all()
    serializer_class = ClaimPlanSerializer


class BankAccountListView(generics.ListAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class BankAccountCreateView(generics.CreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class BankAccountDetailView(generics.RetrieveAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class BankAccountUpdateView(generics.UpdateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class BankAccountDeleteView(generics.DestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionUpdateView(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDeleteView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
