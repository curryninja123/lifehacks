from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'home'
urlpatterns = [
    url(r'^categories/', views.categories, name='categories'),
    url(r'^logout/', views.logout_user, name='logout'),
    url(r'^$', views.index, name='index'),
]
