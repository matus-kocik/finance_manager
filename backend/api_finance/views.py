from rest_framework import generics
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.models import User
from finance.models import *
from .serializers import *


class BaseListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class BaseCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]


class BaseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class TagListView(BaseListAPIView):
    serializer_class = TagSerializer


class TagCreateView(BaseCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IncomeCategoryListView(BaseListAPIView):
    serializer_class = IncomeCategorySerializer


class IncomeCategoryCreateView(generics.CreateAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer
    permission_classes = [IsAuthenticated]


class IncomeCategoryDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer


class ExpenseCategoryListView(BaseListAPIView):
    serializer_class = ExpenseCategorySerializer


class ExpenseCategoryCreateView(BaseCreateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class ExpenseCategoryDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class FinancialSourceListView(BaseListAPIView):
    serializer_class = FinancialSourceSerializer


class FinancialSourceCreateView(BaseCreateAPIView):
    queryset = FinancialSource.objects.all()
    serializer_class = FinancialSourceSerializer


class FinancialSourceDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = FinancialSource.objects.all()
    serializer_class = FinancialSourceSerializer


class IncomePlanListView(BaseListAPIView):
    serializer_class = IncomePlanSerializer


class IncomePlanCreateView(BaseCreateAPIView):
    queryset = IncomePlan.objects.all()
    serializer_class = IncomePlanSerializer


class IncomePlanDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = IncomePlan.objects.all()
    serializer_class = IncomePlanSerializer


class IncomeListView(BaseListAPIView):
    serializer_class = IncomeSerializer


class IncomeCreateView(BaseCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class IncomeDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class ExpensePlanListView(BaseListAPIView):
    serializer_class = ExpensePlanSerializer


class ExpensePlanCreateView(BaseCreateAPIView):
    queryset = ExpensePlan.objects.all()
    serializer_class = ExpensePlanSerializer


class ExpensePlanDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = ExpensePlan.objects.all()
    serializer_class = ExpensePlanSerializer


class ExpenseListView(BaseListAPIView):
    serializer_class = ExpenseSerializer


class ExpenseCreateView(BaseCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class InvestmentListView(BaseListAPIView):
    serializer_class = InvestmentSerializer


class InvestmentCreateView(BaseCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class InvestmentDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class InvestmentPlanListView(BaseListAPIView):
    serializer_class = InvestmentPlanSerializer


class InvestmentPlanCreateView(BaseCreateAPIView):
    queryset = InvestmentPlan.objects.all()
    serializer_class = InvestmentPlanSerializer


class InvestmentPlanDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = InvestmentPlan.objects.all()
    serializer_class = InvestmentPlanSerializer


class DebtListView(BaseListAPIView):
    serializer_class = DebtSerializer


class DebtCreateView(BaseCreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class DebtDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class DebtPlanListView(BaseListAPIView):
    serializer_class = DebtPlanSerializer


class DebtPlanCreateView(BaseCreateAPIView):
    queryset = DebtPlan.objects.all()
    serializer_class = DebtPlanSerializer


class DebtPlanDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = DebtPlan.objects.all()
    serializer_class = DebtPlanSerializer


class ClaimListView(BaseListAPIView):
    serializer_class = ClaimSerializer


class ClaimCreateView(BaseCreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ClaimDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ClaimPlanListView(BaseListAPIView):
    serializer_class = ClaimPlanSerializer


class ClaimPlanCreateView(BaseCreateAPIView):
    queryset = ClaimPlan.objects.all()
    serializer_class = ClaimPlanSerializer


class ClaimPlanDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = ClaimPlan.objects.all()
    serializer_class = ClaimPlanSerializer


class BankAccountListView(BaseListAPIView):
    serializer_class = BankAccountSerializer


class BankAccountCreateView(BaseCreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class BankAccountDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class TransactionListView(BaseListAPIView):
    serializer_class = TransactionSerializer


class TransactionCreateView(BaseCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailUpdateDeleteView(BaseRetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
