from django.db import models
import random

def generate_unique_ra():
    while True:
        ra = str(random.randint(10**9, 10**10 - 1))  # Gera um RA de 10 dígitos
        if not client.objects.filter(ra=ra).exists():
            return ra

class client (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email= models.EmailField(null=True, max_length=254)
    ra = models.CharField(max_length=10, unique=True, default=generate_unique_ra)
    
    def __str__(self):
        return self.usuario.username