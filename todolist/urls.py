from django.urls import path
from . import views

urlpatterns = [
    path('', views.leer),
    path('leer', views.leer, name="leer"),
    path('guardar', views.guardar, name="guardar"),
    path('modificar', views.modificar, name="modificar"),
    path('eliminar', views.eliminar, name="eliminar")
]
