from django.urls import path, include
from .views import (
                store_view,
            )

app_name = 'store'
urlpatterns = [
    path('', store_view, name="store"),
]
