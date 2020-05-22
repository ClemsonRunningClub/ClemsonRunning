from django.contrib import admin

# Register your models here.
from .models import Point #relative Import

admin.site.register(Point)
