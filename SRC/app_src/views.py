from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Client


# Verifica se o usuario logado é dono do objeto a ser visto na DB ou se ele é superuser.
def is_owner():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            cliente = get_object_or_404(Client, id=kwargs.get("id", None))

            # Verifica se o usuário é administrador (superuser)
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            # Verifica se o usuario tem o mesmo nome do objeto (owner)
            if request.user.id == cliente.contractor.id:
                print("pass")
                return view_func(request, *args, **kwargs)
            else:
                return redirect("dashboard")  # 403 Redireciona para a página de login

        return _wrapped_view

    return decorator


# ------------------------------VIEWS----------------------------------


@login_required
def dashboard(request):
    clientes = Client.objects.filter(contractor=request.user)
    return render(request, "app_src/dashboard.html", {"clientes": clientes})


@login_required
def clientes_create(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        sobrenome = request.POST["sobrenome"]
        email = request.POST["email"]
        telefone = request.POST["telefone"]
        empresa = request.POST["empresa"]
        descricao = request.POST["descricao"]
        cliente = Client(
            contractor=request.user,
            firstname=nome,
            lastname=sobrenome,
            email=email,
            telephone=telefone,
            interprise=empresa,
            description=descricao,
        )
        cliente.save()
        messages.info(request, "Cliente criado com sucesso")
        return redirect("dashboard")
    else:
        return render(request, "app_src/clientes_create.html")


@login_required
@is_owner()
def clientes_edit(request, id):
    cliente = get_object_or_404(Client, id=id)
    if request.method == "POST":
        cliente.firstname = request.POST["nome"]
        cliente.lastname = request.POST["sobrenome"]
        cliente.email = request.POST["email"]
        cliente.telephone = request.POST["telefone"]
        cliente.interprise = request.POST["empresa"]
        cliente.description = request.POST["descricao"]
        cliente.save()
        messages.info(request, "Cliente editado com sucesso")
        return redirect("dashboard")
    else:
        return render(request, "app_src/clientes_edit.html", {"cliente": cliente})


@login_required
@is_owner()
def clientes_delete(request, id):
    cliente = get_object_or_404(Client, id=id)
    if request.method == "POST":
        cliente.delete()
        return redirect("dashboard")
    return render(request, "app_src/clientes_delete.html", {"cliente": cliente})
