from django.urls import path
from django.urls import include

from rest_framework import routers

from apps.shop import views

router = routers.DefaultRouter()

router.register(r'categories', views.Category)
router.register(r'products', views.Product)

urlpatterns = [
    path('', include(router.urls)),
]
