from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'login'
urlpatterns = [
<<<<<<< HEAD
    url(r'^create/$', views.signup_view, name='create'),
    url(r'^new-user/', views.create_user, name='new_user'),
    url(r'^$', views.login_view, name='login'),
=======
    url(r'^new-login/', views.signup_view, name='signup'),
    url(r'^create/', views.create_user, name='create'),
    url(r'^$', views.login_view, name='index'),
>>>>>>> a822cebcf8996c67607581872fcbae767c12484b
]
