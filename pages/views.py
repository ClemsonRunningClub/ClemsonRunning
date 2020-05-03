from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def racing_view(request, *args, **kwargs):
    return render(request, "racing.html", {})

def membership_view(request, *args, **kwargs):
    return render(request, "membership.html", {})

def service_view(request, *args, **kwargs):
    return render(request, "service.html", {})

def sponsor_view(request, *args, **kwargs):
    return render(request, "sponsors.html", {})

def calendar_view(request, *args, **kwargs):
    return render(request, "info/calendar.html", {})

def current_view(request, *args, **kwargs):
    return render(request, "info/current.html", {})

def prospective_view(request, *args, **kwargs):
    return render(request, "info/prospective.html", {})

def routes_view(request, *args, **kwargs):
    return render(request, "info/routes.html", {})
