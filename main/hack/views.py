from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def new_hack(request):
    return render(request, 'pages/newHack.html')

def new_tip(request):
    return render(request, 'pages/newTip.html')

def post_hack(request):
    p = request.POST
    hack = Hack()
    hack.title = p.get('title', '')
    hack.text = p.get('text', '')
    hack.longitude = p.get('longitude', 0)
    hack.latitude = p.get('latitude', 0)
    hack.picture = p.get('picture', None)
    hack.save()
    context = {
        'success-message': 'You have successfully created the hack ' + hack.title,
        'hack': hack,
    }
    return render(request, 'pages/displayHack.html', context)

def post_tip(request):
    p = request.POST
    tip = Tip()
    tip.title = p.get('title', '')
    tip.text = p.get('text', '')
    tip.start = p.get('start', '')
    tip.end = p.get('end', '')
    tip.longitude = p.get('longitude', 0)
    tip.latitude = p.get('latitude', 0)
    tip.save()
    context = {
        'success-message': 'You have successfully created the tip '  + tip.title,
        'tip': tip,
    }
    return render(request, 'pages/displayTip.html', context)

def index(request):
    return HttpResponse('This is the index')

def display_hack(request, id):
    return HttpResponse()

def display_tip(request, id):
    return HttpResponse()
