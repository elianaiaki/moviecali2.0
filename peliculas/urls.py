from django.urls import path
from . import views

app_name = "peliculas"

urlpatterns = [
    path("agregar/", views.agregar_pelicula, name="agregar"),
    path("<int:id>/", views.detalle_pelicula, name="detalle"),
]