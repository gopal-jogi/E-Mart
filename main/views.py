from django.shortcuts import render
from rest_framework import generics
from main.serializers import *
from main.models import *
# Create your views here.
class VendorList(generics.ListAPIView):
    queryset= Vendor.objects.all()
    serializer_class=VendorSerializer