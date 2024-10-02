from django.shortcuts import redirect, render

def index(request):
    return render(request, 'pages/index.html')

def index2(request):
    return render(request, 'pages/index2.html')