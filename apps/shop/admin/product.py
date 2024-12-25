"""
Category UI Admin
"""
from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.admin import TabularInline


from apps.shop import models
from apps.shop import editor


class ProductImageInline(TabularInline):
    model = models.ProductGallery
    extra = 1


@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    form = editor.Product
    list_display = (
        "name",
        "category_id",
        "price",
        "video_link"
    )
    list_filter = (
        "category_id",
    )
    search_fields = (
        "name",
        "description"
    )
    inlines = [ProductImageInline]

    fieldsets = (
        (None, {
            "fields": ("category_id", "name", "image", "description", "price", "video_link") # noqa
        }),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(models.ProductGallery)
class ProductImageAdmin(ModelAdmin):
    list_display = ("product", "image")
