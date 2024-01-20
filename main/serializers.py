from rest_framework import serializers
from main.models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields=['user', 'address']