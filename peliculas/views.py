from django.shortcuts import render
from django.shortcuts import redirect

# lista en memoria: se resetea cada vez que se reinicia el servidor
peliculas = []

def inicio(request):
    contexto = {"titulo_pagina": "Inicio"}
    return render(request, "peliculas/inicio.html", contexto)

def agregar_pelicula(request):
    if request.method == "POST":
        # tomo cada dato que cargó el usuario en el formulario
        pelicula = {
            "id": len(peliculas) + 1,
            "imagen": request.POST.get("imagen"),
            "titulo": request.POST.get("titulo"),
            "anio": request.POST.get("anio"),
            "duracion": request.POST.get("duracion"),
            "temporadas": request.POST.get("temporadas"),
            "calificacion": request.POST.get("calificacion"),
            "sinopsis": request.POST.get("sinopsis"),
            "genero": request.POST.get("genero"),
            "reparto": request.POST.get("reparto"),
            "clasificacion": request.POST.get("clasificacion"),
            "plataforma": request.POST.get("plataforma"),
        }
        peliculas.append(pelicula)
        return redirect("peliculas:detalle", id=pelicula["id"])

    contexto = {"titulo_pagina": "Agregar nueva pelicula"}
    return render(request, "peliculas/agregar.html", contexto)

def detalle_pelicula(request, id):
    # busco la pelicula por id dentro de la lista en memoria
    pelicula = None
    for p in peliculas:
        if p["id"] == id:
            pelicula = p
            break

    # separo el reparto en una lista para poder recorrerla con {% for %}
    reparto = []
    if pelicula and pelicula["reparto"]:
        reparto = [nombre.strip() for nombre in pelicula["reparto"].split(",") if nombre.strip()]

    contexto = {
        "titulo_pagina": "Detalle de la pelicula",
        "pelicula": pelicula,
        "reparto": reparto,
    }
    return render(request, "peliculas/detalle.html", contexto)