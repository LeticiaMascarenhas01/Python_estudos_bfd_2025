from django.urls import path, include
from .views import UsuarioViewSet, EscolaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'escolas', EscolaViewSet)

urlpatterns = [
path('', include(router.urls)),
]