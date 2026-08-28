from django.shortcuts import render

def agregar_pelicula(request):
    peliculas = [
        {"titulo": "Matrix", "genero": "Ciencia ficción", "anio": 1999},
        {"titulo": "El Padrino", "genero": "Drama", "anio": 1972},
        {"titulo": "Coco", "genero": "Animación", "anio": 2017},
    ]
    contexto = {
        "titulo_pagina": "Películas en MovieCali",
        "peliculas": peliculas
    }
    return render(request, "peliculas/agregar.html", contexto)