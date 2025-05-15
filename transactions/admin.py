from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = ("id", "user", "amount", "currency", "category", "timestamp")
    search_fields = ("user__name", "user__email", "category", "currency")
    list_filter = ("currency", "category", "timestamp")
    ordering = ("-timestamp",)
    readonly_fields = ("id", "timestamp")
