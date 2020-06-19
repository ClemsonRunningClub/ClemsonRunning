from django.urls import path, include
from .views import (
                store_view,
                store_post_view,
                cart_view,
                cart_add_view,
                cart_delete_view,
                checkout_view,
                checkout_confirm_view,
            )

app_name = 'store'
urlpatterns = [
    path('', store_view, name="store"),
    path('checkout/', checkout_view, name="checkout"),
    path('checkout/confirm', checkout_confirm_view, name="checkout_confirm"),
    path('cart/', cart_view, name="cart"),
    path('cart/<int:id>', cart_add_view, name="cart_add"),
    path('remove/<int:itemid>', cart_delete_view, name="cart_delete"),
    path('<int:id>', store_post_view, name="storeDetail"),
]
