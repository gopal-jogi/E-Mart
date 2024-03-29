from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# vendor models
class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(null=True)
    def __str__(self) -> str:
        return self.user.username
# Product Category
class ProductCategory(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)

    def __str__(self) -> str:
        return self.title
    
# Product
class Product(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)
    price=models.FloatField()

    def __str__(self) -> str:
        return self.title