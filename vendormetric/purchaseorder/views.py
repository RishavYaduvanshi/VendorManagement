from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import PurchaseOrder
from rest_framework import viewsets
from  .serializer import PurchaseOrderSerializer, PurchaseOrderAcknowledgeSerializer


class PurchaseOrderView(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    @action(detail=True, methods=["post"])
    def acknowledge(self, request, pk=None):
        
        purchase_order = self.get_object()

        serializer = PurchaseOrderAcknowledgeSerializer(purchase_order, data=request.data, partial=True)

       
        if serializer.is_valid():
            serializer.save()

            # Retrieve the vendor and calculate average response time
            vendor = purchase_order.vendor
            orders = PurchaseOrder.objects.filter(
                vendor=vendor, acknowledgment_date__isnull=False
            )
            acknowledgment_times = [
                (order.acknowledgment_date - order.issue_date).total_seconds()
                for order in orders
            ]

            # Calculate the average response time
            if acknowledgment_times:
                vendor.average_response_time = sum(acknowledgment_times) / len(
                    acknowledgment_times
                )
            else:
                vendor.average_response_time = 0

            # Save the updated vendor instance
            vendor.save()

            # Return a success message
            return Response(
                {
                    "message": "Purchase order acknowledged and average response time recalculated."
                },
                status=status.HTTP_200_OK,
            )
        else:
            # Return an error response if the serializer validation fails
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
