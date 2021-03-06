from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def racing_view(request, *args, **kwargs):
    return render(request, "racing.html", {})

def membership_view(request, *args, **kwargs):
    return render(request, "membership.html", {})

def community_view(request, *args, **kwargs):
    return render(request, "community.html", {})

def calendar_view(request, *args, **kwargs):
    return render(request, "info/calendar.html", {})

def officer_view(request, *args, **kwargs):
    return render(request, "info/officer.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "info/about.html", {})

def routes_view(request, *args, **kwargs):
    return render(request, "info/routes.html", {})
