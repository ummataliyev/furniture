from rest_framework import serializers
from apps.shop import models
from apps.shop.serializers import Category


class ProductGallery(serializers.ModelSerializer):
    class Meta:
        model = models.ProductGallery
        fields = (
            'id',
            'image'
        )


class Product(serializers.ModelSerializer):
    category = Category(read_only=True, source='category_id')
    gallery = ProductGallery(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = (
            'id',
            'category',
            'name',
            'image',
            'description',
            'price',
            'video_link',
            'created_at',
            'updated_at',
            'gallery'
        )
