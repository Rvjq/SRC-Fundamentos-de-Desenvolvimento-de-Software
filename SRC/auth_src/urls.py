from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('plataforma', views.plataforma, name='plataforma'),
    path('login', views.login, name='login'),
]