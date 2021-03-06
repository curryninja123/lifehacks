from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.http import Http404
from . import models
# Create your views here.
def login_view(request):
    return render(request, 'pages/login.html')

def signup_view(request):
	return render(request, 'pages/signup.html', {'error_message': ''})

def create_user(request):
    p = request.POST
    ps, psc = p.get('password', ''), p.get('password_confirm', '')
    if ps != psc:
        return render(request, 'pages/signup.html', {'error_message': 'Passwords do not match.'})
    try:
        user = User()
        user.username = p.get('username', '')
        user.first_name = p.get('first_name', '')
        user.last_name = p.get('last_name', '')
        user.email = p.get('email', '')
        user.password = ps
        if len(ps) < 8:
            return render(request, 'pages/signup.html', {'error_message': 'That password is too short. Please make it 8 characters or longer.'})
        user.save()
        member = models.Member(user=user)
        member.hometown = p.get('hometown', '')
        member.profile_pic = p.get('profile_pic', None)
        member.save()
    except IntegrityError:
        return render(request, 'pages/signup.html', {'error_message': 'There is already a user with username: ' + p.get('username', '') +'.'})
        return render(request, 'pages/signup.html', {'error_message': 'Passwords do not match'})
    member = models.Member(user = User())
    user = member.user
    user.username = p.get('username', '')
    user.first_name = p.get('first_name', '')
    user.last_name = p.get('last_name', '')
    user.email = p.get('email', '')
    user.password = ps
    member.hometown = p.get('hometown', '')
    member.profile_pic = p.get('profile_pic', None)
    return render(request, 'pages/success.html', {'success_message':'created an account!'})

def login_user(request):
    p = request.POST
    username = p.get('username', '')
    password = p.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'pages/success.html', {'success_message':'logged in, ' +username+'!'}) # change later
    else:
        return render(request, 'pages/login.html', {'error_message': 'Incorrect username or password.'})
