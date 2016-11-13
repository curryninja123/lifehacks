from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from hack.models import *

# Create your views here.
def index(request):
    des = []
    for hack in Hack.objects.all():
        if len(hack.text) <= 50:
            des.append(hack.text)
        else:
            des.append(hack.text[:47]+'...')
    context = {
        'hack_list': Hack.objects.all(),
        'tip_list': Tip.objects.all(),
        'hack_des': des,
    }
    return render(request, 'pages/index.html', context)

def home(request):
    return render(request, 'pages/home.html')

def categories(request):
	return render(request, 'pages/categories.html', {})
def logout_user(request):
    logout(request)
    return index(request)

def largest_subsequence(st1, st2):
    if not st1 or not st2:
        return 0
    
