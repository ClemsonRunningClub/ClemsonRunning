"""runningclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import (
                bucks_view,
                bucksReg_view,
                )
#app name was indicated in urls.py since not part of main application urls.py
app_name = 'bucks'

urlpatterns = [
    path('', bucks_view),
    path('register/', bucksReg_view),

    #PASSWORD RESET AND CHANGES
    # (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
            # imported reverse_lazy in order to change the success_url. The success_url needed to be indicated bucks since the app_name indicated within this urls.py doc was 'bucks'
            # wouldn't work without changing it (stackoverflow FTW). NEEDED TO ADD 'bucks:URLNAME' DUE TO BEING WITHIN THE 'bucks' APPLICATION.
            # NAMING SCHEME FOR BELOW FOLLOWS THE REFERENCE GITHUB LINK. WILL NOT WORK IF NAMES OR FILES ARE CHANGED AROUND.
    # password_change_form.html
    path('password/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('bucks:password_change_done')), name='password_change'),
    # password_change_done.html
    path('password/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # password_reset_form.html
    path('reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('bucks:password_reset_done')), name='password_reset'),
    # password_reset_done.html
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # password_reset_confirm.html
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('bucks:password_reset_complete')), name='password_reset_confirm'),
    # password_reset_complete.html
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #needed to be last since these are the default views and django sorts through the views in order. Once found, it returns without looking at the rest.
    #auth views include password changing/reset and login logout. Paths above are custom views for some of the default views.
    path('', include("django.contrib.auth.urls")),
]
