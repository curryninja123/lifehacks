from django.shortcuts import render
from django.contrib.auth.models import User
from . import models
# Create your views here.
def login_view(request):
    return render(request, 'pages/login.html')

def signup_view(request):
	return render(request, 'pages/signup.html')

def create_user(usr, name, mail, pwd, town, pic):
    u = User(username=usr, email=mail, password=pwd, first_name=name[0], last_name=name[1])
    member = Member(user=u, hometown=town, profile_pic=pic)
    member.save()
