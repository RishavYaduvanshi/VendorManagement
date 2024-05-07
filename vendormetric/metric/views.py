from django.shortcuts import render
from rest_framework import viewsets
from .models import VendorPerformance
from .serializer import VendorPerformanceSerializer

# Create your views here.
class MetricView(viewsets.ModelViewSet):
    queryset = VendorPerformance.objects.all()
    serializer_class = VendorPerformanceSerializer
