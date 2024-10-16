from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Tag(
    models.Model
):  # Značka (tag) pre kategorizáciu záznamov v aplikácii finance (Income, Expense, FinancialSource, ...)
    name = models.CharField(
        verbose_name=_("Tag Name"),
        max_length=50,
        unique=True,
        help_text=_("Enter a tag name"),
        error_messages={
            "unique": _(
                "A %(model_name)s with that name '%(value)s' already exists. Please enter a unique %(field_label)s name."
            ),
            "max_length": _(
                "The %(field_label)s name is too long. It must be 50 characters or fewer."
            ),
        },
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True,
        help_text=_("The date and time this tag was created."),
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True,
        help_text=_("The date and time this tag was last updated."),
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ["name"]


class BaseModel(
    models.Model
):  # Základný model pre všetky ďalšie modely v aplikácii finance (Income, Expense, FinancialSource, ...)
    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="%(class)s_users",
        help_text=_("The user who created this record."),
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=64,
        db_index=True,
        help_text=_("Enter a name for this record."),
        error_messages={
            "max_length": _("The name is too long. It must be 64 characters or fewer.")
        },
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        default="",
        help_text=_("Enter a description for this record (optional)."),
    )
    notes = models.TextField(
        verbose_name=_("Notes"),
        blank=True,
        default="",
        help_text=_("Enter notes for this record (optional)."),
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_("Tags"),
        blank=True,
        related_name="%(class)s_tags",
        help_text=_("Select tags for this record (optional)."),
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        max_length=128,
        blank=True,
        help_text=_("Enter a unique slug for this record."),
        error_messages={
            "unique": _(
                "A record with that slug already exists. Please enter a unique slug."
            ),
            "max_length": _(
                "The slug is too long. It must be 128 characters or fewer."
            ),
        },
    )
    PRIORITY_CHOICES = [
        ("low", _("Low")),
        ("medium", _("Medium")),
        ("high", _("High")),
    ]
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="medium",
        verbose_name=_("Priority"),
        help_text=_("Select the priority for this record."),
    )
    is_active = models.BooleanField(
        verbose_name=_("Is Active"), default=True, help_text=_("Is this record active?")
    )
    is_archived = models.BooleanField(
        verbose_name=_("Is Archived"),
        default=False,
        help_text=_("Is this record archived?"),
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True,
        help_text=_("The date and time was created."),
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True,
        help_text=_("The date and time was last updated."),
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def save(
        self, *args, **kwargs
    ):  # Vytvorenie slugu z názvu záznamu (name) pre URL adresu záznamu (detail view) v aplikácii finance (Income, Expense, FinancialSource, ...)
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class IncomeCategory(BaseModel):  # Kategória príjmu
    pass


class ExpenseCategory(BaseModel):  # Kategória výdavku
    pass


class FinancialSource(BaseModel):  # Finančný zdroj
    pass


class IncomePlan(BaseModel):  # Plánovaný príjem
    planned_amount = models.DecimalField(
        verbose_name=_("Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the planned amount for this income_plan."),
        error_messages={
            "max_digits": _("The amount must be 12 digits or fewer."),
            "decimal_places": _("The amount must be 2 decimal places or fewer."),
        },
    )
    planned_monthly_amount = models.DecimalField(
        verbose_name=_("Monthly Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the planned monthly amount for this income_plan."),
        error_messages={
            "max_digits": _("The monthly amount must be 12 digits or fewer."),
            "decimal_places": _(
                "The monthly amount must be 2 decimal places or fewer."
            ),
        },
    )
    planned_payment_date = models.DateField(
        verbose_name=_("Payment Date"),
        default=now,
        help_text=_("Enter the planned payment date for this income_plan."),
    )
    planned_hours = models.DecimalField(
        verbose_name=_("Planned Hours"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the planned hours for this income_plan."),
        error_messages={
            "max_digits": _("The hours must be 6 digits or fewer."),
            "decimal_places": _("The hours must be 2 decimal places or fewer."),
        },
    )
    # TODO: pravdepodobne to sem nepasuje a dam to inde, ...
    planned_hourly_rate = models.DecimalField(
        verbose_name=_("Planned Hourly Rate"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the planned hourly rate for this income_plan."),
        error_messages={
            "max_digits": _("The planned hourly rate must be 6 digits or fewer."),
            "decimal_places": _("The planned hourly rate must be 2 decimal places or fewer."),
        },
    )
    source = models.ForeignKey(
        FinancialSource,
        verbose_name=_("Source"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
        related_name="%(class)s_sources",
        help_text=_("Select the source for this income_plan."),
    )
    category = models.ForeignKey(
        IncomeCategory,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
        related_name="%(class)s_categories",
        help_text=_("Select the category for this income_plan."),
    )
    is_salary = models.BooleanField(
        verbose_name=_("Is Salary"),
        default=False,
        help_text=_("Is this income_plan a salary?"),
    )
    is_claim = models.BooleanField(
        verbose_name=_("Is Claim"),
        default=False,
        help_text=_("Is this income_plan a claim?"),
    )
    is_recurring = models.BooleanField(
        verbose_name=_("Is Recurring"),
        default=False,
        help_text=_("Is this income_plan recurring?"),
    )


class Income(BaseModel):  # Príjem
    amount = models.DecimalField(
        verbose_name=_("Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the amount for this income."),
        error_messages={
            "max_digits": _("The amount must be 12 digits or fewer."),
            "decimal_places": _("The amount must be 2 decimal places or fewer."),
        },
    )
    monthly_amount = models.DecimalField(
        verbose_name=_("Monthly Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the monthly amount for this income."),
        error_messages={
            "max_digits": _("The monthly amount must be 12 digits or fewer."),
            "decimal_places": _(
                "The monthly amount must be 2 decimal places or fewer."
            ),
        },
    )
    payment_date = models.DateField(
        verbose_name=_("Payment Date"),
        default=now,
        help_text=_("Enter the payment date for this income."),
    )
    hours = models.DecimalField(
        verbose_name=_("Hours"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the hours for this income."),
        error_messages={
            "max_digits": _("The hours must be 6 digits or fewer."),
            "decimal_places": _("The hours must be 2 decimal places or fewer."),
        },
    )
    # TODO: pravdepodobne to sem nepasuje a dam to inde, ...
    hourly_rate = models.DecimalField(
        verbose_name=_("Hourly Rate"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the hourly rate for this income."),
        error_messages={
            "max_digits": _("The hourly rate must be 6 digits or fewer."),
            "decimal_places": _("The hourly rate must be 2 decimal places or fewer."),
        },
    )
    source = models.ForeignKey(
        FinancialSource,
        verbose_name=_("Source"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="%(class)s_sources",
        db_index=True,
        help_text=_("Select the source for this income."),
    )
    category = models.ForeignKey(
        IncomeCategory,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="%(class)s_categories",
        db_index=True,
        help_text=_("Select the category for this income."),
    )
    is_salary = models.BooleanField(
        verbose_name=_("Is Salary"),
        default=False,
        help_text=_("Is this income a salary?"),
    )
    is_claim = models.BooleanField(
        verbose_name=_("Is Claim"),
        default=False,
        help_text=_("Is this income a claim?"),
    )
    is_recurring = models.BooleanField(
        verbose_name=_("Is Recurring"),
        default=False,
        help_text=_("Is this income recurring?"),
    )


class ExpensePlan(BaseModel):  # Plánovaný výdavok
    planned_amount = models.DecimalField(
        verbose_name=_("Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the planned amount for this expense_plan."),
        error_messages={
            "max_digits": _("The amount must be 12 digits or fewer."),
            "decimal_places": _("The amount must be 2 decimal places or fewer."),
        },
    )
    planned_monthly_amount = models.DecimalField(
        verbose_name=_("Monthly Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the planned monthly amount for this expense_plan."),
        error_messages={
            "max_digits": _("The monthly amount must be 12 digits or fewer."),
            "decimal_places": _(
                "The monthly amount must be 2 decimal places or fewer."
            ),
        },
    )
    planned_payment_date = models.DateField(verbose_name=_("Planned Payment day"))
    source = models.ForeignKey(
        FinancialSource,
        verbose_name=_("Source"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
        related_name="%(class)s_sources",
        help_text=_("Select the source for this expense_plan."),
    )
    category = models.ForeignKey(
        ExpenseCategory,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
        related_name="%(class)s_categories",
        help_text=_("Select the category for this expense_plan."),
    )
    is_investment = models.BooleanField(
        verbose_name=_("Is Investment"),
        default=False,
        help_text=_("Is this expense_plan an investment?"),
    )
    is_debt = models.BooleanField(
        verbose_name=_("Is Debt"),
        default=False,
        help_text=_("Is this expense_plan a debt?"),
    )
    is_recurring = models.BooleanField(
        verbose_name=_("Is Recurring"),
        default=False,
        help_text=_("Is this expense_plan recurring?"),
    )


class Expense(BaseModel):  # Výdavok
    amount = models.DecimalField(
        verbose_name=_("Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the amount for this expense."),
        error_messages={
            "max_digits": _("The amount must be 12 digits or fewer."),
            "decimal_places": _("The amount must be 2 decimal places or fewer."),
        },
    )
    monthly_amount = models.DecimalField(
        verbose_name=_("Monthly Amount"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the monthly amount for this expense."),
        error_messages={
            "max_digits": _("The monthly amount must be 12 digits or fewer."),
            "decimal_places": _(
                "The monthly amount must be 2 decimal places or fewer."
            ),
        },
    )
    payment_date = models.DateField(verbose_name=_("Payment Date"), default=now)
    source = models.ForeignKey(
        FinancialSource,
        verbose_name=_("Source"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
        related_name="%(class)s_sources",
        help_text=_("Select the source for this expense."),
    )
    category = models.ForeignKey(
        ExpenseCategory,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
        related_name="%(class)s_categories",
        help_text=_("Select the category for this expense."),
    )
    is_paid = models.BooleanField(
        verbose_name=_("Is Paid"), default=False, help_text=_("Is this expense paid?")
    )
    is_investment = models.BooleanField(
        verbose_name=_("Is Investment"),
        default=False,
        help_text=_("Is this expense an investment?"),
    )
    is_debt = models.BooleanField(
        verbose_name=_("Is Debt"), default=False, help_text=_("Is this expense a debt?")
    )
    is_recurring = models.BooleanField(
        verbose_name=_("Is Recurring"),
        default=False,
        help_text=_("Is this expense recurring?"),
    )


class InvestmentPlan(BaseModel):  # Plánovaná investícia
    planned_expense = models.OneToOneField(
        ExpensePlan,
        verbose_name=_("Planned Expense"),
        on_delete=models.CASCADE,
        related_name="investment_plans",
        help_text=_("Select the planned expense for this investment_plan."),
    )
    goal = models.DecimalField(
        verbose_name=_("Investment Goal"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the investment goal for this investment_plan."),
        error_messages={
            "max_digits": _("The investment goal must be 12 digits or fewer."),
            "decimal_places": _(
                "The investment goal must be 2 decimal places or fewer."
            ),
        },
    )
    balance = models.DecimalField(
        verbose_name=_("Current Balance"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the current balance for this investment_plan."),
        error_messages={
            "max_digits": _("The current balance must be 12 digits or fewer."),
            "decimal_places": _(
                "The current balance must be 2 decimal places or fewer."
            ),
        },
    )
    percent_change = models.DecimalField(
        verbose_name=_("Percent Change"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the percent change for this investment_plan."),
        error_messages={
            "max_digits": _("The percent change must be 6 digits or fewer."),
            "decimal_places": _(
                "The percent change must be 2 decimal places or fewer."
            ),
        },
    )


class Investment(BaseModel):  # Investícia
    expense = models.OneToOneField(
        Expense,
        verbose_name=_("Expense"),
        on_delete=models.CASCADE,
        related_name="investments",
        help_text=_("Select the expense for this investment."),
    )
    goal = models.DecimalField(
        verbose_name=_("Investment Goal"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the investment goal for this investment."),
        error_messages={
            "max_digits": _("The investment goal must be 12 digits or fewer."),
            "decimal_places": _(
                "The investment goal must be 2 decimal places or fewer."
            ),
        },
    )
    balance = models.DecimalField(
        verbose_name=_("Current Balance"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the current balance for this investment."),
        error_messages={
            "max_digits": _("The current balance must be 12 digits or fewer."),
            "decimal_places": _(
                "The current balance must be 2 decimal places or fewer."
            ),
        },
    )
    percent_change = models.DecimalField(
        verbose_name=_("Percent Change"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the percent change for this investment."),
        error_messages={
            "max_digits": _("The percent change must be 6 digits or fewer."),
            "decimal_places": _(
                "The percent change must be 2 decimal places or fewer."
            ),
        },
    )


class DebtPlan(BaseModel):  # Plánovaný dlh
    planned_expense = models.OneToOneField(
        ExpensePlan,
        verbose_name=_("Planned Expense"),
        on_delete=models.CASCADE,
        related_name="debt_plans",
        help_text=_("Select the planned expense for this debt_plan."),
    )
    planned_creditor = models.CharField(
        verbose_name=_("Planned Creditor"),
        max_length=128,
        blank=True,
        db_index=True,
        help_text=_("Enter the planned creditor for this debt_plan."),
        error_messages={
            "max_length": _(
                "The creditor name is too long. It must be 128 characters or fewer."
            )
        },
    )
    interest_rate = models.DecimalField(
        verbose_name=_("Planned Interest Rate"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the planned interest rate for this debt_plan."),
        error_messages={
            "max_digits": _("The interest rate must be 6 digits or fewer."),
            "decimal_places": _("The interest rate must be 2 decimal places or fewer."),
        },
    )
    planned_due_date = models.DateField(
        verbose_name=_("Planned Due Date"),
        blank=True,
        null=True,
        help_text=_("Enter the planned due date for this debt_plan."),
    )
    planned_start_date = models.DateField(
        verbose_name=_("Planned Start Date"),
        blank=True,
        null=True,
        help_text=_("Enter the planned start date for this debt_plan."),
    )
    planned_end_date = models.DateField(
        verbose_name=_("Planned End Date"),
        blank=True,
        null=True,
        help_text=_("Enter the planned end date for this debt_plan."),
    )


class Debt(BaseModel):  # Dlh
    expense = models.OneToOneField(
        Expense,
        on_delete=models.CASCADE,
        related_name="debts",
        help_text=_("Select the expense for this debt."),
    )
    creditor = models.CharField(
        verbose_name=_("Creditor"),
        max_length=128,
        blank=True,
        db_index=True,
        help_text=_("Enter the creditor for this debt."),
        error_messages={
            "max_length": _(
                "The creditor name is too long. It must be 128 characters or fewer."
            )
        },
    )
    interest_rate = models.DecimalField(
        verbose_name=_("Interest Rate"),
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the interest rate for this debt."),
        error_messages={
            "max_digits": _("The interest rate must be 6 digits or fewer."),
            "decimal_places": _("The interest rate must be 2 decimal places or fewer."),
        },
    )
    due_date = models.DateField(
        verbose_name=_("Due Date"),
        blank=True,
        null=True,
        help_text=_("Enter the due date for this debt."),
    )
    start_date = models.DateField(
        verbose_name=_("Start Date"),
        blank=True,
        null=True,
        help_text=_("Enter the start date for this debt."),
    )
    end_date = models.DateField(
        verbose_name=_("End Date"),
        blank=True,
        null=True,
        help_text=_("Enter the end date for this debt."),
    )


class ClaimPlan(BaseModel):  # Plánovaná pohľadávka
    planned_income = models.OneToOneField(
        IncomePlan,
        on_delete=models.CASCADE,
        related_name="claim_plans",
        help_text=_("Select the planned income for this claim_plan."),
    )
    planned_debtor = models.CharField(
        verbose_name=_("Planned Debtor"),
        max_length=128,
        blank=True,
        db_index=True,
        help_text=_("Enter the planned debtor for this claim_plan."),
        error_messages={
            "max_length": _(
                "The debtor name is too long. It must be 128 characters or fewer."
            )
        },
    )
    planned_interest_rate = models.DecimalField(
        verbose_name=_("Planned Interest Rate"),
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the planned interest rate for this claim_plan."),
        error_messages={
            "max_digits": _("The interest rate must be 5 digits or fewer."),
            "decimal_places": _("The interest rate must be 2 decimal places or fewer."),
        },
    )
    planned_due_date = models.DateField(
        verbose_name=_("Planned Due Date"),
        blank=True,
        null=True,
        help_text=_("Enter the planned due date for this claim_plan."),
    )
    planned_start_date = models.DateField(
        verbose_name=_("Planned Start Date"),
        blank=True,
        null=True,
        help_text=_("Enter the planned start date for this claim_plan."),
    )
    planned_end_date = models.DateField(
        verbose_name=_("Planned End Date"),
        blank=True,
        null=True,
        help_text=_("Enter the planned end date for this claim_plan."),
    )


class Claim(BaseModel):  # Pohľadávka
    income = models.OneToOneField(
        Income,
        on_delete=models.CASCADE,
        related_name="claims",
        help_text=_("Select the income for this claim."),
    )
    debtor = models.CharField(
        verbose_name=_("Debtor"),
        max_length=128,
        blank=True,
        db_index=True,
        help_text=_("Enter the debtor for this claim."),
        error_messages={
            "max_length": _(
                "The debtor name is too long. It must be 128 characters or fewer."
            )
        },
    )
    interest_rate = models.DecimalField(
        verbose_name=_("Interest Rate"),
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the interest rate for this claim."),
        error_messages={
            "max_digits": _("The interest rate must be 5 digits or fewer."),
            "decimal_places": _("The interest rate must be 2 decimal places or fewer."),
        },
    )
    due_date = models.DateField(
        verbose_name=_("Due Date"),
        blank=True,
        null=True,
        help_text=_("Enter the due date for this claim."),
    )
    start_date = models.DateField(
        verbose_name=_("Start Date"),
        blank=True,
        null=True,
        help_text=_("Enter the start date for this claim."),
    )
    end_date = models.DateField(
        verbose_name=_("End Date"),
        blank=True,
        null=True,
        help_text=_("Enter the end date for this claim."),
    )


class BankAccount(BaseModel):  # Bankový účet
    bank_name = models.CharField(
        verbose_name=_("Bank Name"),
        max_length=64,
        blank=True,
        help_text=_("Enter the bank name for this bank_account."),
        error_messages={
            "max_length": _(
                "The bank name is too long. It must be 64 characters or fewer."
            )
        },
    )
    iban = models.CharField(
        verbose_name=_("IBAN"),
        max_length=34,
        blank=True,
        help_text=_("Enter the IBAN for this bank_account."),
        error_messages={
            "max_length": _("The IBAN is too long. It must be 34 characters or fewer.")
        },
    )
    balance = models.DecimalField(
        verbose_name=_("Balance"),
        max_digits=12,
        decimal_places=2,
        blank=True,
        default=0,
        help_text=_("Enter the balance for this bank_account."),
        error_messages={
            "max_digits": _("The balance must be 12 digits or fewer."),
            "decimal_places": _("The balance must be 2 decimal places or fewer."),
        },
    )
    currency = models.CharField(
        verbose_name=_("Currency"),
        max_length=16,
        blank=True,
        default="EUR",
        help_text=_("Enter the currency for this bank_account."),
        error_messages={
            "max_length": _(
                "The currency is too long. It must be 16 characters or fewer."
            )
        },
    )


class Transaction(BaseModel):
    TRANSACTION_TYPE_CHOICES = [("income", "Income"), ("expense", "Expense")]

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
        verbose_name=_("Transaction Type"),
        help_text=_("Select the transaction type."),
    )
    bank_account = models.ForeignKey(
        BankAccount,
        verbose_name=_("Bank Account"),
        on_delete=models.CASCADE,
        related_name="transactions",
        help_text=_("Select the bank account for this transaction."),
    )
    related_income = models.ForeignKey(
        Income,
        verbose_name=_("Related Income"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text=_("Select the related income for this transaction."),
    )
    related_expense = models.ForeignKey(
        Expense,
        verbose_name=_("Related Expense"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text=_("Select the related expense for this transaction."),
    )

    def clean(self):
        if self.transaction_type == "income" and not self.related_income:
            raise ValidationError(
                _("Related income is required for income transaction.")
            )
        if self.transaction_type == "expense" and not self.related_expense:
            raise ValidationError(
                _("Related expense is required for expense transaction.")
            )
        if self.related_income and self.related_expense:
            raise ValidationError(
                _("A transaction cannot be related to both income and expense.")
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
