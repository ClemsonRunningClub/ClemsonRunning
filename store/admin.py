from django.contrib import admin
from .models import StorePost, Cart, Order
admin.site.register(StorePost)
admin.site.register(Order)
admin.site.register(Cart)
