from django.shortcuts import render
from django.contrib.auth.models import User
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
        return render(request, 'pages/signup.html', {'error_message': 'Passwords do not match'})
    user = User()
    user.username = p.get('username', '')
    user.first_name = p.get('first_name', '')
    user.last_name = p.get('last_name', '')
    user.email = p.get('email', '')
    user.password = ps
    user.save()
    member = models.Member(user=user)
    member.hometown = p.get('hometown', '')
    member.profile_pic = p.get('profile_pic', None)
    member.save()
    return render(request, 'pages/success.html')
