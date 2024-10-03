from rest_framework import generics
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.models import User
from finance.models import *
from .serializers import *


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class TagListView(generics.ListAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagDetailView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class TagUpdateView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class TagDeleteView(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class IncomeCategoryListView(generics.ListAPIView):
    serializer_class = IncomeCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class IncomeCategoryCreateView(generics.CreateAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer
    permission_classes = [IsAuthenticated]


class IncomeCategoryDetailView(generics.RetrieveAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer
    permission_classes = [IsAuthenticated, IsOwner]


class IncomeCategoryUpdateView(generics.UpdateAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer
    permission_classes = [IsAuthenticated, IsOwner]


class IncomeCategoryDeleteView(generics.DestroyAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ExpenseCategoryListView(generics.ListAPIView):
    serializer_class = ExpenseCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class ExpenseCategoryCreateView(generics.CreateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    permission_classes = [IsAuthenticated]


class ExpenseCategoryDetailView(generics.RetrieveAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ExpenseCategoryUpdateView(generics.UpdateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ExpenseCategoryDeleteView(generics.DestroyAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    permission_classes = [IsAuthenticated, IsOwner]


class FinancialSourceListView(generics.ListAPIView):
    serializer_class = FinancialSourceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class FinancialSourceCreateView(generics.CreateAPIView):
    queryset = FinancialSource.objects.all()
    serializer_class = FinancialSourceSerializer
    permission_classes = [IsAuthenticated]


class FinancialSourceDetailView(generics.RetrieveAPIView):
    queryset = FinancialSource.objects.all()
    serializer_class = FinancialSourceSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class FinancialSourceUpdateView(generics.UpdateAPIView):
    queryset = FinancialSource.objects.all()
    serializer_class = FinancialSourceSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class FinancialSourceDeleteView(generics.DestroyAPIView):
    queryset = FinancialSource.objects.all()
    serializer_class = FinancialSourceSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class IncomePlanListView(generics.ListAPIView):
    serializer_class = IncomePlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class IncomePlanCreateView(generics.CreateAPIView):
    queryset = IncomePlan.objects.all()
    serializer_class = IncomePlanSerializer
    permission_classes = [IsAuthenticated]


class IncomePlanDetailView(generics.RetrieveAPIView):
    queryset = IncomePlan.objects.all()
    serializer_class = IncomePlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class IncomePlanUpdateView(generics.UpdateAPIView):
    queryset = IncomePlan.objects.all()
    serializer_class = IncomePlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class IncomePlanDeleteView(generics.DestroyAPIView):
    queryset = IncomePlan.objects.all()
    serializer_class = IncomePlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class IncomeListView(generics.ListAPIView):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class IncomeCreateView(generics.CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]


class IncomeDetailView(generics.RetrieveAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class IncomeUpdateView(generics.UpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class IncomeDeleteView(generics.DestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ExpensePlanListView(generics.ListAPIView):
    serializer_class = ExpensePlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class ExpensePlanCreateView(generics.CreateAPIView):
    queryset = ExpensePlan.objects.all()
    serializer_class = ExpensePlanSerializer
    permission_classes = [IsAuthenticated]


class ExpensePlanDetailView(generics.RetrieveAPIView):
    queryset = ExpensePlan.objects.all()
    serializer_class = ExpensePlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ExpensePlanUpdateView(generics.UpdateAPIView):
    queryset = ExpensePlan.objects.all()
    serializer_class = ExpensePlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ExpensePlanDeleteView(generics.DestroyAPIView):
    queryset = ExpensePlan.objects.all()
    serializer_class = ExpensePlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ExpenseListView(generics.ListAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class ExpenseCreateView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]


class ExpenseDetailView(generics.RetrieveAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ExpenseUpdateView(generics.UpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ExpenseDeleteView(generics.DestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class InvestmentListView(generics.ListAPIView):
    serializer_class = InvestmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class InvestmentCreateView(generics.CreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    permission_classes = [IsAuthenticated]


class InvestmentDetailView(generics.RetrieveAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class InvestmentUpdateView(generics.UpdateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class InvestmentDeleteView(generics.DestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class InvestmentPlanListView(generics.ListAPIView):
    serializer_class = InvestmentPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class InvestmentPlanCreateView(generics.CreateAPIView):
    queryset = InvestmentPlan.objects.all()
    serializer_class = InvestmentPlanSerializer
    permission_classes = [IsAuthenticated]


class InvestmentPlanDetailView(generics.RetrieveAPIView):
    queryset = InvestmentPlan.objects.all()
    serializer_class = InvestmentPlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class InvestmentPlanUpdateView(generics.UpdateAPIView):
    queryset = InvestmentPlan.objects.all()
    serializer_class = InvestmentPlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class InvestmentPlanDeleteView(generics.DestroyAPIView):
    queryset = InvestmentPlan.objects.all()
    serializer_class = InvestmentPlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class DebtListView(generics.ListAPIView):
    serializer_class = DebtSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class DebtCreateView(generics.CreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    permission_classes = [IsAuthenticated]


class DebtDetailView(generics.RetrieveAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class DebtUpdateView(generics.UpdateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class DebtDeleteView(generics.DestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class DebtPlanListView(generics.ListAPIView):
    serializer_class = DebtPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class DebtPlanCreateView(generics.CreateAPIView):
    queryset = DebtPlan.objects.all()
    serializer_class = DebtPlanSerializer
    permission_classes = [IsAuthenticated]


class DebtPlanDetailView(generics.RetrieveAPIView):
    queryset = DebtPlan.objects.all()
    serializer_class = DebtPlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class DebtPlanUpdateView(generics.UpdateAPIView):
    queryset = DebtPlan.objects.all()
    serializer_class = DebtPlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class DebtPlanDeleteView(generics.DestroyAPIView):
    queryset = DebtPlan.objects.all()
    serializer_class = DebtPlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ClaimListView(generics.ListAPIView):
    serializer_class = ClaimSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class ClaimCreateView(generics.CreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [IsAuthenticated]


class ClaimDetailView(generics.RetrieveAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ClaimUpdateView(generics.UpdateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ClaimDeleteView(generics.DestroyAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ClaimPlanListView(generics.ListAPIView):
    serializer_class = ClaimPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class ClaimPlanCreateView(generics.CreateAPIView):
    queryset = ClaimPlan.objects.all()
    serializer_class = ClaimPlanSerializer
    permission_classes = [IsAuthenticated]


class ClaimPlanDetailView(generics.RetrieveAPIView):
    queryset = ClaimPlan.objects.all()
    serializer_class = ClaimPlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ClaimPlanUpdateView(generics.UpdateAPIView):
    queryset = ClaimPlan.objects.all()
    serializer_class = ClaimPlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ClaimPlanDeleteView(generics.DestroyAPIView):
    queryset = ClaimPlan.objects.all()
    serializer_class = ClaimPlanSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class BankAccountListView(generics.ListAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class BankAccountCreateView(generics.CreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]


class BankAccountDetailView(generics.RetrieveAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class BankAccountUpdateView(generics.UpdateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class BankAccountDeleteView(generics.DestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]


class TransactionDetailView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class TransactionUpdateView(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class TransactionDeleteView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, IsOwner]
