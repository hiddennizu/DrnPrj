from django.conf.urls import url
from . import views
from django.contrib.auth.views import password_reset, password_reset_done

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'dashboard/$', views.dashboard, name="dashboard"),
    url(r'login/$', views.user_login, name="login"),
    url(r'logout/$', views.user_logout, name="logout"),
    url(r'register/$', views.user_register, name='register'),
    url(r'pass_change/$', views.chage_password, name='change'),
    url(r'user_list/$', views.user_list, name='user_list'),

]
