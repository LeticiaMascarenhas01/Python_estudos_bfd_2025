from rest_framework import serializers
from.models import Usuario, Escola

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']

class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = [
            'nome', 'cnpj', 'email',
            'data_cadastro', 'plano_assinatura','endereco','telefone', 
            'status_pagamento'
        ]