from django.urls import path
from django.urls import include
from django.contrib import admin
from django.http import HttpResponse
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from src.settings import default


def home(request):
    return HttpResponse("Welcome to the Furniture API!")


schema_view = get_schema_view(
    openapi.Info(
        title="Furniture API",
        default_version="v1",
        description="API documentation for the Furniture application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', home, name='home'),
    path("admin/", admin.site.urls),
    path("api/", include("apps.shop.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]

urlpatterns += static(default.MEDIA_URL, document_root=default.MEDIA_ROOT)
urlpatterns += static(default.STATIC_URL, document_root=default.STATIC_ROOT)
