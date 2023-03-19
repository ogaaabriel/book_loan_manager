from django.contrib import admin

from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
    search_fields = ["title", "author"]
    list_filter = ["author"]


@admin.register(models.Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ["name", "cpf"]
    search_fields = ["name", "cpf"]


@admin.register(models.Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ["book", "borrower", "date_added", "date_return"]
    search_fields = ["book", "borrower"]
    list_filter = ["date_added", "date_return"]
