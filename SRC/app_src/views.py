from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.contrib import messages

def dashboard(request):
    if request.user.is_authenticated:  
        return render(request, 'app_src/dashboard.html')
    else:
        messages.info(request,"Please login first")
        return redirect("login")

def plataforma(request):
    if request.user.is_authenticated:  
        return render(request, 'app_src/plataforma.html')
    else:
        messages.info(request,"Please login first")
        return redirect("login")