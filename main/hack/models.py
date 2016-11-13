from django.db import models
from django import forms
from . import imageform

# Create your models here.

class Tip (models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    start = models.DateTimeField(max_length=50)
    end = models.DateTimeField(max_length=50)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    categories = []

class Hack(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=150)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    picture = models.ImageField(upload_to = 'hack/', default = 'hack/no-img.jpg')
    publisher = models.CharField(max_length=50)
    rates = 0
    rating = 0
    comments = []
    categories = []

class Comment(models.Model):
    text = models.TextField()
    time = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
