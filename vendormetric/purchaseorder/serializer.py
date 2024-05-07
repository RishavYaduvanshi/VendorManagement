from rest_framework import serializers
import uuid
from .models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        exclude = ["po_id"]
        read_only_fields = ["po_number", "order_date"]

    def create(self, validated_data):
        po_number = f'PO-{uuid.uuid4()}'
        validated_data['po_number'] = po_number
        return super().create(validated_data)

class PurchaseOrderAcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['acknowledgment_date', 'status']
