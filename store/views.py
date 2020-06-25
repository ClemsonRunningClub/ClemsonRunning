from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from bucks.models import Point
from .models import StorePost, Cart, Order
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
# Create your views here.

@login_required
def store_view(request):
    account = Point.objects.get(id=request.user.id)
    storePost = StorePost.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'account': account,
        'storePost': storePost

    }
    return render(request, 'store.html', context)

@login_required
def store_post_view(request, id):
    account = Point.objects.get(id=request.user.id)
    storePost = get_object_or_404(StorePost, pk=id)
    context = {
        'account': account,
        'storePost': storePost
    }
    return render(request, 'store_detail.html', context)

@login_required
def cart_add_view(request, id):
    try:
        items = Cart.objects.get(user=request.user)
    except:
        items = Cart.objects.create(user=request.user)
        items.save()

    if items.cartItem1 == None:
        singleItem = StorePost.objects.get(id=id)
        items.cartItem1 = singleItem
        items.cartPrice += singleItem.price
        items.cartCount += 1

    elif items.cartItem2 == None:
        singleItem = StorePost.objects.get(id=id)
        items.cartItem2 = singleItem
        items.cartPrice += singleItem.price
        items.cartCount += 1

    elif items.cartItem3 == None:
        singleItem = StorePost.objects.get(id=id)
        items.cartItem3 = singleItem
        items.cartPrice += singleItem.price
        items.cartCount += 1

    elif items.cartItem4 == None:
        singleItem = StorePost.objects.get(id=id)
        items.cartItem4 = singleItem
        items.cartPrice += singleItem.price
        items.cartCount += 1

    elif items.cartItem5 == None:
        singleItem = StorePost.objects.get(id=id)
        items.cartItem5 = singleItem
        items.cartPrice += singleItem.price
        items.cartCount += 1

    elif items.cartCount >= 5:
        error = "You have too many items in your cart. Please remove one to add a different one!"
        context = {
            'error':error,
            'items':items
        }
        return render(request, 'cart.html', context)
    items.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def cart_delete_view(request, itemid):
    items = Cart.objects.get(user=request.user)
    if itemid == 1:
        items.cartPrice -= items.cartItem1.price
        items.cartItem1 = None
        items.cartCount -= 1
    elif itemid == 2:
        items.cartPrice -= items.cartItem2.price
        items.cartItem2 = None
        items.cartCount -= 1
    elif itemid == 3:
        items.cartPrice -= items.cartItem3.price
        items.cartItem3 = None
        items.cartCount -= 1
    elif itemid == 4:
        items.cartPrice -= items.cartItem4.price
        items.cartItem4 = None
        items.cartCount -= 1
    elif itemid == 5:
        items.cartPrice -= items.cartItem5.price
        items.cartItem5 = None
        items.cartCount -= 1

    items.save()
    return redirect('store:cart')

@login_required
def cart_view(request):
    try:
        items = Cart.objects.get(user=request.user)
    except:
        items = Cart.objects.create(user=request.user)
        items.save()
    context = {
            'items':items,
        }
    return render(request, 'cart.html', context)

@login_required
def checkout_view(request):
    items = Cart.objects.get(user=request.user)
    if items.cartPrice == 0:
        return redirect('store:cart')
    context = {
            'items':items,
        }
    return render(request, 'checkout.html', context)

@login_required
def checkout_confirm_view(request):
    account = Point.objects.get(user=request.user)
    items = Cart.objects.get(user=request.user)
    if items.cartPrice > account.total:
        return HttpResponse("<h1>ERROR: Your balance is too low</h1>")
    else:
        order = Order.objects.create(user=request.user)
        account.total -= items.cartPrice
        if items.cartItem1:
            order.item1 = items.cartItem1.title
        if items.cartItem2:
            order.item2 = items.cartItem2.title
        if items.cartItem3:
            order.item3 = items.cartItem3.title
        if items.cartItem4:
            order.item4 = items.cartItem4.title
        if items.cartItem5:
            order.item5 = items.cartItem5.title

        order.orderTotal = items.cartPrice
        order.orderNum = get_random_string(length=10, allowed_chars='1234567890')
        order.save()
        account.save()
        items.delete()
        send_mail(
            'BUCKS ORDER PLACED | CLEMSON RUNNING CLUB',
            'We have received your order. Order confirmation number: ' + order.orderNum,
            'run@g.clemson.edu',
            [request.user.email],
            fail_silently=False
            )
    return render(request, 'order_placed.html', {'order':order})
