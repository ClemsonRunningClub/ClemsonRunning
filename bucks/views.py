from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, RequestContext
from django.http import HttpResponse, Http404
from .models import Point, Post, Admin_community_code
from .forms import AccountForm, CreateBlog, UpdateBlog, InputCode
from django.contrib.auth.models import User
from operator import attrgetter
from datetime import datetime, time
from .strava_key import client_secret
from django.utils.crypto import get_random_string
from django import forms
import requests
import urllib3
import json
# Create your views here.

# Registration view for running bucks
def bucksReg_view(response):
    if response.method == "POST":
        form = AccountForm(response.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/bucks/login")
    else:
        form = AccountForm()
    return render(response, "bucksReg.html", {"form":form})

# Running bucks home page view

def bucks_view(response):
    if response.user.is_authenticated:
        current_user=response.user
        #is needed since website cannot function if there are 0 total codes generated
        if Admin_community_code.objects.exists():
            #obtains the most recent obtained community code
            code = Admin_community_code.objects.order_by('-id')[0]
        if current_user.id != None:
            point = Point.objects.get(id=current_user.id)
            post  = sorted(Post.objects.filter(), key=attrgetter('date_up'), reverse=True)
            if point in response.user.point.all():
                context = {}
                context['point'] = point
                context['post'] = post
                #is needed since website cannot function if there are 0 total codes generated
                if Admin_community_code.objects.exists():
                    context['code'] = code
                return render(response, "bucks.html", context)
        else:
            return render(response, "bucks.html", {})
    else:
        return redirect("/bucks/login")

# Post views to create, modify or delete

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
        return redirect("/bucks")
    return render(request, "post_create.html", {"form":form})


def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detail_post.html', {'post':post})

def update_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.author:
        if request.POST:
            form = UpdateBlog(request.POST or None, request.FILES or None, instance=post)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                post = obj
                return redirect("/bucks")
        form = UpdateBlog(
            initial = {
                "title": post.title,
                "body": post.body,
                "image": post.image,
            }
        )
        return render(request, 'update_post.html', {"form":form})


def delete_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.author:
        post.delete()
    return redirect("/bucks")

#community views
def input_view(response):
    #obtains the most recent obtained community code
    admin_code = Admin_community_code.objects.order_by('-id')[0]
    if response.method == "POST":
        form = InputCode(response.POST or None)
        if form.is_valid():
            if str(form.cleaned_data['community_code']) == str(admin_code):
                account = Point.objects.get(id=response.user.id)
                #this will determine if the user tries to enter a code they already obtained community bucks for. No double dippers.
                if str(account.community_code) == str(admin_code):
                    error = "No unlimited bucks glitch. This isn't GTA."
                    return render(response, 'community_input.html', {'form':form, 'error':error})

                account.community_code = form.cleaned_data['community_code']
                account.community = account.community + 5
                account.total = float(account.total) + 5
                account.save()
                return redirect("/bucks")
            error = 'The code that you entered is invalid. Please try again!'
            return render(response, 'community_input.html', {'form':form, 'error':error})
    form = InputCode
    return render(response, 'community_input.html', {'form':form})

def generate_view(request):
    code = Admin_community_code.objects.create()
    code.generated_code = get_random_string(length=6, allowed_chars='1234567890')
    code.save()
    return redirect("/bucks")

#strava views

# ran when connecting to strava the first time
def strava_connect(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    return redirect('https://www.strava.com/oauth/authorize?client_id=48474&response_type=code&redirect_uri=http://localhost:8000/bucks/exchange_token&approval_prompt=force&scope=read,activity:read_all,profile:read_all,read_all')
# once the user accepts the request, the following connects the strava account the model "Point" that is connected to the user
def strava_code(request):
    code = request.GET.get('code')
    #redirects back to bucks if the user selects cancel on the authorization screen for strava
    if request.GET.get('error'):
        return redirect("/bucks")
    auth_url = "https://www.strava.com/oauth/token?"
    activites_url = "https://www.strava.com/api/v3/athlete/activities"

    # Strava documentation (ref: https://developers.strava.com/docs/authentication/#requestingaccess)
    payload = {
        'client_id': "48474",
        'client_secret': client_secret,
        'code': code,
        'grant_type': 'authorization_code',
    }
    #obtains the refresh_token by using the payload above
    account = Point.objects.get(id=request.user.id)
    athlete_data = requests.post(auth_url, data=payload).json()
    refresh_token = athlete_data['refresh_token']
    athlete_id = athlete_data['athlete']['id']
    account. athlete_id   = athlete_id
    account.refresh_token = refresh_token
    payload_refresh = {
        'client_id': "48474",
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token',
    }
    #uses refresh token to obtain access_token
    access_token = requests.post(auth_url, data=payload_refresh).json()['access_token']
    account.access_token = access_token
    # Strava request data parameters (ref: https://developers.strava.com/docs/reference/)
    # initial request to find grab information
    header = {'Authorization': 'Bearer ' + access_token}
    #the after variable must be in epoch time, subtracts 104400 so the user gains strava runs 24 hours before account creation.
    param = {'per_page': 200, 'page': 1, 'after': int(request.user.date_joined.strftime("%s"))-104400,}
    data = requests.get(activites_url, headers=header, params=param).json()
    #obtains the distances and times for the runs requested after the time indicated
    #only obtains the runs from the user, not all activities
    distance_arr=[d['distance'] for d in data if d['type']=='Run']
    time_arr=[d['start_date_local'] for d in data]

    time_arr_length = len(time_arr)
    #obtains the latest run time
    if time_arr_length > 0:
        time_latest = time_arr[time_arr_length-1]
        #converts the time_latest to epoch time
        epoch_latest = datetime.strptime(time_latest,"%Y-%m-%dT%H:%M:%SZ").strftime("%s")
        account.epoch = epoch_latest
    distance_ran_meters = sum(distance_arr)
    distance_ran_miles = round(distance_ran_meters/1609, 2)
    account.miles = distance_ran_miles

    try:
        account.save()
    except:
        return HttpResponse('<h1>Please use a different strava to sign in. This strava is already connected to a user</h1>')

    account.total = float(account.miles) + float(account.community)
    account.strava_connected = True
    account.save()
    return redirect('bucks:home')

# This allows for the refresh of the strava api to display the proper data.
def strava_refresh(request):
    auth_url = "https://www.strava.com/oauth/token?"
    activites_url = "https://www.strava.com/api/v3/athlete/activities"
    account = Point.objects.get(id=request.user.id)

    payload_update_refresh = {
        'client_id': "48474",
        'client_secret': client_secret,
        'refresh_token': account.refresh_token,
        'grant_type': 'refresh_token',
        }
    #uses refresh token to obtain access_token (access_tokens are good for only 1 hour and need to be updated hence the repetition in code)
    access_token = requests.post(auth_url, data=payload_update_refresh).json()['access_token']
    account.access_token = access_token
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1, 'after': account.epoch,}
    data = requests.get(activites_url, headers=header, params=param).json()
    #obtains the distances and times for the runs requested after the time indicated only if there is new runs available
    if len(data) > 0 and int(account.epoch) > 0:
        distance_arr=[d['distance'] for d in data if d['type']=='Run']
        time_arr=[d['start_date_local'] for d in data]

        time_arr_length = len(time_arr)
        #obtains the latest run time
        time_latest = time_arr[time_arr_length-1]
        #converts the time_latest to epoch time
        epoch_latest = datetime.strptime(time_latest,"%Y-%m-%dT%H:%M:%SZ").strftime("%s")
        account.epoch = epoch_latest
        distance_ran_meters = sum(distance_arr)
        distance_ran_miles = round(distance_ran_meters/1609, 2)
        account.total = float(account.total) + float(distance_ran_miles)
        account.miles = float(account.miles) + float(distance_ran_miles)
        account.save()

    return redirect('bucks:home')
