from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'hack'
urlpatterns = [
    url(r'^create_hack/$', views.new_hack, name='new_hack'),
    url(r'^create_tip/$', views.new_tip, name='new_tip'),
    url(r'^post_tip/$', views.create_tip, name='create_tip'),
    url(r'^post_hack/$', views.create_hack, name='create_hack'),
    url(r'^$', views.index, name='index'),
    url(r'^view/(?P<wisdom_id>[0-9]+)', views.display, name='display'),

]
