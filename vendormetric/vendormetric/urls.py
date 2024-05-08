from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vendor.views import VendorViewSet
from purchaseorder.views import PurchaseOrderView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r"purchase_orders", PurchaseOrderView)
urlpatterns = [
    path("api/docs/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/swagger-ui/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
