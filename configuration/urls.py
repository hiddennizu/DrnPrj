from django.conf.urls import url, include
from django.contrib import admin
from configuration import views

urlpatterns = [
    url(r'', views.configuration, name='configuration'),
]
