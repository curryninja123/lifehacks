from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'hack'
urlpatterns = [
    url(r'^new_hack/', views.new_hack, name='new_hack'),
    url(r'^new_tip/', views.new_tip, name='new_tip'),
    url(r'^post_hack/', views.post_hack, name='post_hack'),
    url(r'^post_tip/', views.post_tip, name='post_tip'),
    url(r'^view_hack/(?P<hack_id>[0-9]+)/primary/', views.display_hack, name='display_hack'),
    url(r'^view_tip/(?P<tip_id>[0-9]+)/primary/', views.display_tip, name='display_tip'),
    url(r'^$', views.index, name='index'),
]
