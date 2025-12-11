from django.db import models

class Users(models.Model):
    nome = models.CharField(primary_key = True, max_length = 12, editable = True)
    emails = models.EmailField(max_length = 100, blank = False, null = False)
    senha = models.CharField(max_length = 100, blank = False, null = False)

    def __str__(self):
        return self.nome
    
class Escola_Fu(models.Model):

    nome= models.CharField(max_length=50, blank=False, null=False)
    cnpj= models.CharField(max_length=18, unique=True, blank=False, null=False)
    email= models.EmailField(max_length=100, blank=False, null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    plano_assinatura =models.CharField(
        max_length=50,
        choices=[
            ('Básico', 'Básico'),
            ('Premium', 'Premium'),
            ('Pro', 'Pro')
        ],
        default='Básico'
)
endereco= models.CharField(max_length=200, blank=True, null=True)
telefone= models.CharField(max_length=20, blank=True, null=True)
status_pagamento = models.BooleanField(default=False) 

def _str_(self):
    return self.nome