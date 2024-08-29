from django.db import models
from django_cryptography.fields import encrypt
from django.utils.timezone import now
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(verbose_name=_("Tag Name"), max_length=50, unique=True)
    created_at = models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated At"), auto_now=True)

    def __str__(self):
        return f"{self.name}"


class BaseModel(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_("Name"), max_length=64)
    description = models.TextField(verbose_name=_("Description"), blank=True)
    notes = models.TextField(verbose_name=_("Notes"), blank=True)
    tags = models.ManyToManyField(Tag, verbose_name=_("Tags"), blank=True)
    slug = models.SlugField(
        verbose_name=_("Slug"), unique=True, max_length=128, blank=True
    )
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="medium",
        verbose_name=_("Priority"),
    )
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)
    is_archived = models.BooleanField(verbose_name=_("Is Archived"), default=False)
    created_at = models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated At"), auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class IncomeCategory(BaseModel):  # Kategória príjmu
    pass


class ExpenseCategory(BaseModel):  # Kategória výdavku
    pass


class FinancialSource(BaseModel):  # Zdroj
    pass


class IncomePlan(BaseModel):  # Plánovaný príjem
    planned_amount = models.DecimalField(
        verbose_name=_("Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
    )
    planned_monthly_amount = models.DecimalField(
        verbose_name=_("Monthly Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
    )
    planned_payment_date = models.DateField(verbose_name=_("Payment Date"))
    planned_hours = models.DecimalField(
        verbose_name=_("Planned Hours"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
    )
    planned_hourly_rate = encrypt(
        models.DecimalField(
            verbose_name=_("Planned Hourly Rate"),
            max_digits=6,
            decimal_places=2,
            blank=True,
            default=0,
        )
    )
    source = models.ForeignKey(
        FinancialSource, verbose_name=_("Source"), on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        IncomeCategory, verbose_name=_("Category"), on_delete=models.CASCADE
    )
    is_salary = models.BooleanField(verbose_name=_("Is Salary"), default=False)
    is_claim = models.BooleanField(verbose_name=_("Is Claim"), default=False)
    is_recurring = models.BooleanField(verbose_name=_("Is Recurring"), default=False)


class Income(BaseModel):  # Príjem
    amount = models.DecimalField(
        verbose_name=_("Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
    )
    monthly_amount = models.DecimalField(
        verbose_name=_("Monthly Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
    )
    payment_date = models.DateField(verbose_name=_("Payment Date"), default=now)
    hours = models.DecimalField(
        verbose_name=_("Hours"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
    )
    hourly_rate = encrypt(
        models.DecimalField(
            verbose_name=_("Hourly Rate"),
            max_digits=6,
            decimal_places=2,
            blank=True,
            default=0,
        )
    )
    source = models.ForeignKey(
        FinancialSource, verbose_name=_("Source"), on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        IncomeCategory, verbose_name=_("Category"), on_delete=models.CASCADE
    )
    is_salary = models.BooleanField(verbose_name=_("Is Salary"), default=False)
    is_claim = models.BooleanField(verbose_name=_("Is Claim"), default=False)
    is_recurring = models.BooleanField(verbose_name=_("Is Recurring"), default=False)


class ExpensePlan(BaseModel):  # Plánovaný výdavok
    planned_amount = models.DecimalField(
        verbose_name=_("Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
    )
    planned_monthly_amount = models.DecimalField(
        verbose_name=_("Monthly Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
    )
    planned_payment_date = models.DateField(verbose_name=_("Planned Payment day"))
    source = models.ForeignKey(
        FinancialSource, verbose_name=_("Source"), on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        ExpenseCategory, verbose_name=_("Category"), on_delete=models.CASCADE
    )
    is_investment = models.BooleanField(verbose_name=_("Is Investment"))
    is_debt = models.BooleanField(verbose_name=_("Is Debt"))
    is_recurring = models.BooleanField(verbose_name=_("Is Recurring"), default=False)


class Expense(BaseModel):  # Výdavok
    amount = models.DecimalField(
        verbose_name=_("Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
    )
    monthly_amount = models.DecimalField(
        verbose_name=_("Monthly Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
    )
    payment_date = models.DateField(verbose_name=_("Payment Date"), default=now)
    source = models.ForeignKey(
        FinancialSource, verbose_name=_("Source"), on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        ExpenseCategory, verbose_name=_("Category"), on_delete=models.CASCADE
    )
    is_paid = models.BooleanField(verbose_name=_("Is Paid"), default=False)
    is_investment = models.BooleanField(verbose_name=_("Is Investment"))
    is_debt = models.BooleanField(verbose_name=_("Is Debt"))
    is_recurring = models.BooleanField(verbose_name=_("Is Recurring"), default=False)


class InvestmentPlan(BaseModel):  # Plánovaná investícia
    planned_expense = models.OneToOneField(
        Expense, verbose_name=_("Planned Expense"), on_delete=models.CASCADE
    )
    planned_investment_date = models.DateField(
        verbose_name=_("Planned Investment Date"), blank=True, null=True
    )


class Investment(BaseModel):  # Investícia
    expense = models.OneToOneField(
        Expense, verbose_name=_("Expense"), on_delete=models.CASCADE
    )
    investment_date = models.DateField(
        verbose_name=_("Investment Date"), blank=True, null=True
    )


class DebtPlan(models.Model):  # Plánovaný dlh
    planned_expense = models.OneToOneField(ExpensePlan, on_delete=models.CASCADE)
    interest_rate = models.DecimalField(
        verbose_name=_("Planned Interest Rate"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
    )
    planned_due_date = models.DateField(
        verbose_name=_("Planned Due Date"), blank=True, null=True
    )
    planned_start_date = models.DateField(
        verbose_name=_("Planned Start Date"), blank=True, null=True
    )
    planned_end_date = models.DateField(
        verbose_name=_("Planned End Date"), blank=True, null=True
    )
    planned_creditor = models.CharField(
        verbose_name=_("Planned Creditor"), max_length=128, blank=True
    )


class Debt(models.Model):  # Dlh
    expense = models.OneToOneField(Expense, on_delete=models.CASCADE)
    interest_rate = models.DecimalField(
        verbose_name=_("Interest Rate"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
    )
    due_date = models.DateField(verbose_name=_("Due Date"), blank=True, null=True)
    start_date = models.DateField(verbose_name=_("Start Date"), blank=True, null=True)
    end_date = models.DateField(verbose_name=_("End Date"), blank=True, null=True)
    creditor = models.CharField(verbose_name=_("Creditor"), max_length=128, blank=True)


class ClaimPlan(models.Model):  # Plánovaná pohľadávka
    planned_income = models.OneToOneField(IncomePlan, on_delete=models.CASCADE)
    planned_interest_rate = models.DecimalField(
        verbose_name=_("Planned Interest Rate"),
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=0,
    )
    planned_due_date = models.DateField(
        verbose_name=_("Planned Due Date"), blank=True, null=True
    )
    planned_start_date = models.DateField(
        verbose_name=_("Planned Start Date"), blank=True, null=True
    )
    planned_end_date = models.DateField(
        verbose_name=_("Planned End Date"), blank=True, null=True
    )
    planned_debtor = models.CharField(
        verbose_name=_("Planned Debtor"), max_length=128, blank=True
    )


class Claim(models.Model):  # Pohľadávka
    income = models.OneToOneField(Income, on_delete=models.CASCADE)
    interest_rate = models.DecimalField(
        verbose_name=_("Interest Rate"),
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=0,
    )
    due_date = models.DateField(verbose_name=_("Due Date"), blank=True, null=True)
    start_date = models.DateField(verbose_name=_("Start Date"), blank=True, null=True)
    end_date = models.DateField(verbose_name=_("End Date"), blank=True, null=True)
    debtor = models.CharField(verbose_name=_("Debtor"), max_length=128, blank=True)


class BankAccount(BaseModel):  # Bankový účet
    bank_name = models.CharField(verbose_name=_("Bank Name"), max_length=64)
    iban = encrypt(models.CharField(verbose_name=_("IBAN"), max_length=34))
    balance = encrypt(
        models.DecimalField(
            verbose_name=_("Balance"),
            max_digits=12,
            decimal_places=2,
            blank=True,
            default=0,
        )
    )
    currency = models.CharField(verbose_name=_("Currency"), max_length=16, blank=True)


class Transaction(BaseModel):
    TRANSACTION_TYPE_CHOICES = [("income", "Income"), ("expense", "Expense")]

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
        verbose_name=_("Transaction Type"),
    )
    bank_account = models.ForeignKey(
        BankAccount, verbose_name=_("Bank Account"), on_delete=models.CASCADE
    )
    related_income = models.ForeignKey(
        Income,
        verbose_name=_("Related Income"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    related_expense = models.ForeignKey(
        Expense,
        verbose_name=_("Related Expense"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        amount = 0
        if self.transaction_type == "income" and self.related_income:
            if self.related_income.is_recurring:
                amount = self.related_income.monthly_amount
            else:
                amount = self.related_income.amount
            self.bank_account.balance += amount
        elif self.transaction_type == "expense" and self.related_expense:
            if self.related_expense.is_recurring:
                amount = self.related_expense.monthly_amount
            else:
                amount = self.related_expense.amount
            self.bank_account.balance -= amount
        self.bank_account.save()
        super().save(*args, **kwargs)
