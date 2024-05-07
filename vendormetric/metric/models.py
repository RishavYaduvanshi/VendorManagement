from django.db import models
from vendor.models import Vendor

# Create your models here.

"""
● vendor: ForeignKey - Link to the Vendor model.
● date: DateTimeField - Date of the performance record.
● on_time_delivery_rate: FloatField - Historical record of the on-time delivery rate.
● quality_rating_avg: FloatField - Historical record of the quality rating average.
● average_response_time: FloatField - Historical record of the average response
time.
● fulfillment_rate: FloatField - Historical record of the fulfilment rate.
"""
class VendorPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.vendor.name
