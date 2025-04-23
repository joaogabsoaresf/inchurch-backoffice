from django.db import models

class RoleChoices(models.TextChoices):
    SUPERADMIN = "superadmin", "Super Admin"
    ADMIN = "admin", "Admin"
    BASIC = "basic", "Básico"

class TeamChoices(models.TextChoices):
    MARKETING = "marketing", "Marketing"
    SALES = "sales", "Vendas"
    CS = "cs", "CS"
    SUPPORT = "support", "Suporte"
    FINANCE = "finance", "Financeiro"
    BI = "bi", "BI"
    HR = "hr", "RH"
    TECH = "tech", "Tecnologia"
    OTHER = "other", "Outro"
    SARA = "sara", "Sara"

class CurrencyChoices(models.TextChoices):
    BRL = "brl", "BRL"
    USD = "usd", "USD"
    EUR = "eur", "EUR"