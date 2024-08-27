from django.db import models
from django_cryptography.fields import encrypt
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=64)
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name


class IncomePlan: # Plánovaný príjem
    pass


class Income(BaseModel): # Príjem
    amount = models.DecimalField(verbose_name=_("Amount"), max_digits=12, decimal_places=2)
    payment_date = models.DateField(verbose_name=_("Payment Date"), default=now)
    source = encrypt(models.ForeignKey("FinancialSource", verbose_name=_("Source"), on_delete=models.CASCADE))
    category = encrypt(models.ForeignKey("IncomeCategory", verbose_name=_("Category"),  on_delete=models.CASCADE))


class ExpensePlan: # Plánovaný výdavok
    pass


class Expense(BaseModel): # Výdavok
    amount = models.DecimalField(verbose_name=_("Amount"), max_digits=12, decimal_places=2)
    payment_date = models.DateField(verbose_name=_("Payment Date"), default=now)
    source = models.ForeignKey("FinancialSource", verbose_name=_("Source"), on_delete=models.CASCADE)
    category = models.ForeignKey("ExpenseCategory", verbose_name=_("Category"), on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name=_("Is Paid"), default=False)


class BankAccount(BaseModel): # Bankový účet
    bank_name = models.CharField(verbose_name=_("Bank Name"), max_length=64)
    iban = encrypt(models.CharField(verbose_name=_("IBAN"), max_length=34))
    balance = encrypt(models.DecimalField(verbose_name=_("Balance"), max_digits=12, decimal_places=2))
    currency = models.CharField(verbose_name=_("Currency"), max_length=16)
    account_type = models.CharField(verbose_name=_("Account Type"), max_length=64)


class InvestmentPlan: # Plánovaná investícia
    pass


class Investment(BaseModel): # Investícia
    amount = models.DecimalField(verbose_name=_("Amount"), max_digits=12, decimal_places=2)
    investment_date = models.DateField(verbose_name=_("Investment Date"), auto_now=False, auto_now_add=False)
    is_paid = models.BooleanField(verbose_name=_("Is Paid"), default=False)


class IncomeCategory(BaseModel): # Kategória príjmu
    pass


class ExpenseCategory(BaseModel): # Kategória výdavku
    pass


class FinancialSource(BaseModel): # Zdroj
    pass


class Debt(BaseModel): # Dlh
    pass


class Claim(BaseModel): # Pohľadávka
    pass