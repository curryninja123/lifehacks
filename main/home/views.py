from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from hack.models import *

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def home(request):
    return render(request, 'pages/home.html')

def categories(request):
	return render(request, 'pages/categories.html', {})
def logout_user(request):
    logout(request)
    return HttpResponse('You have been usccessfully logged out.')
