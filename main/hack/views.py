from django.shortcuts import render
from .models import *
from django.db import models
import datetime
# Create your views here.
def index(request):
    return render(request, 'pages/create.html')

def display(request, wisdom_id):
    w = Wisdom.objects.get(pk=wisdom_id)
    context = {
        'wisdom': w,
    }
    return render(request, 'pages/display.html', context)

def new_hack(request):
    return render(request, 'pages/createHack.html')

def new_tip(request):
    return render(request, 'pages/createTip.html')

def create_tip(request):
    p = request.POST
    tip = Tip()
    tip.title = p.get('title', '')
    tip.longitude = p.get('longitude', 0)
    tip.latitude = p.get('latitude', 0)
    tip.text = p.get('text', '')
    tip.start = p.get('start', datetime.now())
    tip.end = p.get('end', datetime.now())
    tip.save()
    return render()

def create_hack(request):
    p = request.POST
