from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from purchaseorder.models import PurchaseOrder
from .models import Vendor
from django.db import models
from django.db.models import Avg
from .serializer import VendorSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(detail=True, methods=["get"])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        orders = PurchaseOrder.objects.filter(vendor=vendor, status="Delivered")

        # Calculate performance metrics
        total_orders = orders.count()
        if total_orders:
            on_time_deliveries = orders.filter(delivery_date__lte=models.F('delivery_date')).count()
            on_time_delivery_rate = (on_time_deliveries / total_orders) * 100

            quality_rating_avg = (
                orders.aggregate(Avg("quality_rating"))["quality_rating__avg"] or 0
            )

            acknowledgment_times = [
                (order.acknowledgment_date - order.issue_date).total_seconds()
                for order in orders
                if order.acknowledgment_date
            ]
            average_response_time = (
                sum(acknowledgment_times) / len(acknowledgment_times)
                if acknowledgment_times
                else 0
            )

            fulfillment_rate = (
                orders.filter(status="completed").count() / total_orders * 100
            )
        else:
            on_time_delivery_rate = 0
            quality_rating_avg = 0
            average_response_time = 0
            fulfillment_rate = 0

        
        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.quality_rating_avg = quality_rating_avg
        vendor.average_response_time = average_response_time
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()
        return Response(VendorSerializer(vendor).data)
