from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('plataforma', views.plataforma, name='plataforma'),
]