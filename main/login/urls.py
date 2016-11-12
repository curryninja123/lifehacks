from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.login_view, name='index'),
    url(r'^new-login/', views.signup_view, name='signup')
]
