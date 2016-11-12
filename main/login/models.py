from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    hometown = models.CharField(max_length=25)
    profile_pic = models.ImageField()
    password = forms.CharField(widget=forms.PasswordInput())
    radius = 0.5
