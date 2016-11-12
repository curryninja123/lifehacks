from django.contrib.auth.models import User
from django.db import models
from django import forms

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hometown = models.CharField(max_length=25)
    profile_pic = models.ImageField()
    radius = 0.5

    def __str__(self):
        return self.user.get_username()
