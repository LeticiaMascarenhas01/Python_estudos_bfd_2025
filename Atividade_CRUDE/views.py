from rest_framework import viewsets
from .models import Usuario, Escola
from serializer import UsuarioSerializer

class UsuarioViewset(viewsets.ModoViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EscolaViewset(viewsets.ModoViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer