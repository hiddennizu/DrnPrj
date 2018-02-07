from django.conf.urls import url, include
from django.contrib import admin
from Course import views

urlpatterns = [
    url(r'^$', views.course_home, name='course'),

    url(r'^course/new/$', views.course_new, name='course_new'),
    url(r'^courses/$', views.course_list, name='course_list'),
    url(r'^course/(?P<pk>\d+)/edit/$', views.course_edit, name='course_edit'),
    url(r'^course/(?P<pk>\d+)/delete/$', views.course_delete, name='course_delete'),
    url(r'^books/create/$', views.book_create, name='book_create'),

]
