from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'data_analysis/login.html'}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^accounts/profile', views.index, name='profile'),
    url(r'^$', views.index, name='index'),
]