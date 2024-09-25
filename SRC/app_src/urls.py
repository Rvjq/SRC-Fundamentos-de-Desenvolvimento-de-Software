from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('clientes/create', views.clientes_create, name='clientes_create'),
    path('plataforma', views.plataforma, name='plataforma'),
]