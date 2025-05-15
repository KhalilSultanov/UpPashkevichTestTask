from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import UserModel


@admin.register(UserModel)
class UserModelAdmin(ModelAdmin):
    list_display = ("id", "name", "email", "created_at", "updated_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
