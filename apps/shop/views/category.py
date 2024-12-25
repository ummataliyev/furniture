from rest_framework import viewsets

from apps.shop import models
from apps.shop.serializers import category


class Category(viewsets.ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = category.Category
