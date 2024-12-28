"""
Product Table
"""
from django.db import models

from apps.shop.models.category import Category


class Product(models.Model):
    category_id = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта"
    )
    image = models.ImageField(
        upload_to="media/banner/",
        verbose_name="Изображение продукта"
    )
    description = models.TextField(verbose_name="Описание продукта")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена продукта"
    )
    video_link = models.URLField(
        verbose_name="Ссылка на видео",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductGallery(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="gallery",
        on_delete=models.CASCADE,
        verbose_name="Галерея продуктов"
    )
    image = models.ImageField(
        upload_to="media/products/",
        verbose_name="Галерея"
    )

    def __str__(self):
        return f"Image for {self.product.name}"

    class Meta:
        verbose_name = "Галерея продуктов"
        verbose_name_plural = "Галереи продуктов"
