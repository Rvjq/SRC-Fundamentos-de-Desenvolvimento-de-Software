from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Client

def dashboard(request):
    if request.user.is_authenticated:  
        clientes = Client.objects.filter(contractor=request.user) 
        return render(request, 'app_src/dashboard.html', {'clientes': clientes})
    else:
        messages.info(request,"Please login first")
        return redirect("login")

def plataforma(request):
    if request.user.is_authenticated:  
        return render(request, 'app_src/plataforma.html')
    else:
        messages.info(request,"Please login first")
        return redirect("login")
      
def clientes_create(request):
    if request.user.is_authenticated:  
        if request.method == "POST":
            nome = request.POST["nome"]
            sobrenome = request.POST["sobrenome"]
            email = request.POST["email"]
            telefone = request.POST["telefone"]
            empresa = request.POST["empresa"]
            descricao = request.POST["descricao"]
            cliente = Client(contractor=request.user, firstname=nome, lastname=sobrenome, email=email, telephone=telefone, interprise=empresa, description=descricao)
            cliente.save()
            messages.info(request,"Cliente criado com sucesso")
            return redirect("dashboard")
        else:
            return render(request, 'app_src/clientes_create.html')
    else:
        messages.info(request,"Please login first")
        return redirect("login")