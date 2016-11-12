from django.shortcuts import render
from .models import *
from django.db import models
from .forms import *
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
    form = HackForm()

def new_tip(request):
    p = request.POST
