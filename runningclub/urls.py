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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import (
                home_view,
                racing_view,
                calendar_view,
                officer_view,
                about_view,
                routes_view,
                membership_view,
                community_view,
                )

urlpatterns = [
    path('bucks/', include('bucks.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view),

    path('racing/', racing_view, name="racing"),
    path('community/', community_view, name="community"),
    path('info/calendar/', calendar_view, name="calendar"),
    path('membership/', membership_view, name="membership"),
    path('info/officers/', officer_view, name="officer"),
    path('info/about/', about_view, name="about"),
    path('info/routes/', routes_view, name="routes"),
]

if settings.DEBUG==True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
