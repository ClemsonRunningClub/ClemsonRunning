from django.contrib import admin

# Register your models here.
from .models import Account #relative Import

admin.site.register(Account)
