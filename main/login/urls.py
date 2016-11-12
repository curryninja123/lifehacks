from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^new-login/', views.signup_view, name='signup'),
    url(r'^create/', views.create_user, name='create'),
    url(r'^$', views.login_view, name='index'),
]
