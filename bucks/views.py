from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Account
from .forms import AccountForm

# Create your views here.

def bucksPre_view(request):
    initial_data = {
        'account_user': "",
        'password': "",
        'email': "",
    }
    form = AccountForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = AccountForm()
    context = {
        'form':form
    }
    return render(request, "bucksPre.html", context)
