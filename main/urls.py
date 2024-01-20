from django.urls import path
from main.views import *

urlpatterns = [
    path('vendors/',VendorList.as_view()),
]
