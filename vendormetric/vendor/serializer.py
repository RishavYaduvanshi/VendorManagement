from rest_framework import serializers
from .models import Vendor
import uuid

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        exclude = ["vender_id"]
        read_only_fields = ["on_time_delivery_rate", "quality_rating_avg", "average_response_time", "fulfillment_rate", "vendor_code"]

    def create(self, validated_data):
        print(validated_data)
        vendor_code = f"VENDOR-{uuid.uuid4()}"
        validated_data["vendor_code"] = vendor_code
        print(validated_data)
        return super().create(validated_data)
