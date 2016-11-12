from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    return render(request, 'pages/create.html')

def add_comment(wisdom, comment):
    wisdom.comment_list.append(comment)

def 
