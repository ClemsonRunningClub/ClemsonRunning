from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Account
from .forms import AccountForm

# Create your views here.

def bucksReg_view(response):
    if response.method == "POST":
        form = AccountForm(response.POST or None)
        if form.is_valid():
            form.save()
        return redirect("/bucks/login")
    else:
        form = AccountForm()

    return render(response, "bucksReg.html", {"form":form})

def bucks_view(request):
    return render(request, "bucks.html", {})
