from django.db import models
from django.contrib.auth.models import User
import random

def generate_unique_ra():
    while True:
        ra = str(random.randint(10**9, 10**10 - 1))  # Gera um RA de 10 dígitos
        if not Client.objects.filter(ra=ra).exists():
            return ra

class Client (models.Model):
    contractor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contractor')
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email= models.EmailField(null=True, max_length=254)
    telephone = models.CharField(max_length=20)
    interprise = models.CharField(max_length=100)
    description = models.TextField(null=True, max_length=1000)
    ra = models.CharField(max_length=10, unique=True, default=generate_unique_ra)
    
    def __str__(self):
        return "Client: %s, Contractor: %s" %self.firstname % self.contractor.username