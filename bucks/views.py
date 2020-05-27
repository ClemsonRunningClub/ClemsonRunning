from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Point
from .forms import AccountForm, CreateBlog
from django.contrib.auth.models import User

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


def bucks_view(response):
    if response.user.is_authenticated:
        current_user=response.user
        if current_user.id != None:
            point = Point.objects.get(id=current_user.id)
            if point in response.user.point.all():
                return render(response, "bucks.html", {"point":point})
        else:
            return render(response, "bucks.html", {})
    else:
        return redirect("/bucks/login")

def post_create(request):
    current_user = request.user
    if not current_user.is_authenticated:
        return redirect('login')
    form = CreateBlog(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = request.user
        obj.author = author
        obj.save()
        form = CreateBlog()
    return render(request, "post_create.html", {"form":form})
