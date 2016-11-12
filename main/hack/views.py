from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'pages/create.html')

def display(request, wisdom_id):
    w = Wisdom.objects.get(pk=wisdom_id)
    context = {
        'wisdom': w,
        'hack': isinstance(w, Hack),
    }
    return render(request, 'pages/display.html', context)
