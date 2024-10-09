from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home (request):
    return render(request, 'home/home.html')

def signin (request):
    return render(request, 'signin/signin.html')

def signup (request):
    return render(request, 'signup/signup.html')

def resetPass (request):
    return render(request, 'resetPass/reset.html')