from django.shortcuts import render
# Create your views here.
def login_view(request):
    return render(request, 'pages/login.html')

def signup_view(request):
	return render(request, 'pages/signup.html')
