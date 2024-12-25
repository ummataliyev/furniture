from rest_framework import viewsets

from apps.shop import models
from apps.shop.serializers import product


class Product(viewsets.ReadOnlyModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = product.Product
