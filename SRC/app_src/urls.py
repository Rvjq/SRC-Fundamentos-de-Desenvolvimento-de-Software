from django.urls import path

from . import views

urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("clientes/create", views.clientes_create, name="clientes_create"),
    path("clientes/delete/<int:id>/", views.clientes_delete, name="clientes_delete"),
    path("clientes/edit/<int:id>/", views.clientes_edit, name="clientes_edit"),
]
