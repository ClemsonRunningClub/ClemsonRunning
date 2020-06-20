from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from django.contrib.auth.models import  User
# Create your models here.

class StorePost(models.Model):
    title       = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField(blank=True)
    price       = models.IntegerField()
    photo_main  = models.ImageField()
    photo_1     = models.ImageField(blank=True)
    is_published= models.BooleanField(default=True)
    list_date   = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    user             = models.ForeignKey(User, unique=None, on_delete=models.CASCADE, related_name="order", null=True)
    item1            = models.CharField(max_length=100, null=True, blank=True)
    item2            = models.CharField(max_length=100, null=True, blank=True)
    item3            = models.CharField(max_length=100, null=True, blank=True)
    item4            = models.CharField(max_length=100, null=True, blank=True)
    item5            = models.CharField(max_length=100, null=True, blank=True)
    orderNum         = models.IntegerField(null=True, blank=True, default=0)
    orderTotal       = models.IntegerField(null=True, blank=True, default=0)
    orderDate        = models.DateTimeField(default=datetime.now, verbose_name="date ordered")

    def __str__(self):
        return str(self.orderNum)

class Cart(models.Model):
    user             = models.ForeignKey(User, unique=None, on_delete=models.CASCADE, related_name="cart", null=True)
    cartItem1        = models.ForeignKey(StorePost, on_delete=models.CASCADE, related_name="cart1", null=True, blank=True)
    cartItem2        = models.ForeignKey(StorePost, on_delete=models.CASCADE, related_name="cart2", null=True, blank=True)
    cartItem3        = models.ForeignKey(StorePost, on_delete=models.CASCADE, related_name="cart3", null=True, blank=True)
    cartItem4        = models.ForeignKey(StorePost, on_delete=models.CASCADE, related_name="cart4", null=True, blank=True)
    cartItem5        = models.ForeignKey(StorePost, on_delete=models.CASCADE, related_name="cart5", null=True, blank=True)
    cartCount        = models.IntegerField(null=True, blank=True, default=0)
    cartPrice        = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.user.get_username()
