from django.db import models

class Income(models.Model): # Príjem
    pass

class IncomeCategory(models.Model): # Kategória príjmu
    pass

class Expense(models.Model): # Výdavok
    pass

class ExpenseCategory(models.Model): # Kategória výdavku
    pass

class FinancialSource(models.Model): # Zdroj
    pass

class Investment(models.Model): # Investícia
    pass

class Debt(models.Model): # Dlh
    pass

class Claim(models.Model): # Pohľadávka
    pass