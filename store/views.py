from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def store_view(request):
    return render(request, 'store.html', {})
