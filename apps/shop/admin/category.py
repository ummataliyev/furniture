"""
Category UI Admin
"""
from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.shop import models


@admin.register(models.Category)
class Category(ModelAdmin):
    """
    Category UI
    """
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
