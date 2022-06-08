from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    productCode = models.CharField(max_length=100)
    price = models.FloatField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Customer(models.Model):
    user= models.OneToOneField(User, null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    profilepic= models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Status(models.Model):
    name = models.CharField(max_length=100)
    date_create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Order(models.Model):
    orderCode = models.CharField(max_length=100)
    orderDate = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    def __str__(self):
        return self.orderCode


