from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.contrib import messages

def dashboard(request):
    return render(request, 'app_src/dashboard.html')