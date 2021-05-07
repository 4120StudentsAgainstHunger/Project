"""sah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from sahbackend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.volunteer_list),
    url(r'^sahbackend/volunteers/$', views.volunteer_list),
    url(r'^sahbackend/volunteers/(?P<pk>[0-9]+)$', views.getVolunteer),
    path('fliers/', views.flier_list),
    url(r'^sahbackend/fliers/$', views.flier_list),
    url(r'^sahbackend/fliers/(?P<pk>[0-9]+)$', views.getFlier),
    path('blogpages/', views.blogpage_list),
    url(r'^sahbackend/blogpages/$', views.blogpage_list),
    url(r'^sahbackend/blogpages/(?P<pk>[0-9]+)$', views.getBlogPage),
    path('reservations/', views.reservation_list),
    url(r'^sahbackend/reservations/$', views.reservation_list),
    url(r'^sahbackend/reservations/(?P<pk>[0-9]+)$', views.getReservation),
    path('locations/', views.location_list),
    url(r'^sahbackend/locations/$', views.location_list),
    url(r'^sahbackend/locations/(?P<pk>[0-9]+)$', views.getLocation),
    path('events/', views.event_list),
    url(r'^sahbackend/events/$', views.event_list),
    url(r'^sahbackend/events/(?P<pk>[0-9]+)$', views.getEvent),
    path('institutions/', views.institution_list),
    url(r'^sahbackend/institutions/$', views.institution_list),
    url(r'^sahbackend/institutions/(?P<pk>[0-9]+)$', views.getInstitution),
    path('volunteers/', views.volunteer_list),
    url(r'^sahbackend/volunteers/$', views.volunteer_list),
    url(r'^sahbackend/volunteers/(?P<pk>[0-9]+)$', views.getVolunteer),
    path('foodrequests/', views.foodrequest_list),
    url(r'^sahbackend/foodrequests/$', views.foodrequest_list),
    url(r'^sahbackend/foodrequests/(?P<pk>[0-9]+)$', views.getFoodRequest),
]
