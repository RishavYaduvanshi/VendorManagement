from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vendor.views import VendorViewSet
from purchaseorder.views import PurchaseOrderView

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r"purchase_orders", PurchaseOrderView)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
