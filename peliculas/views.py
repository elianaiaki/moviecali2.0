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

#------------------------------------------------------------------------------------------------#
# Lista global temporal (simula la base de datos) para que persista la informacion
RESENAS_LISTA = [
    {
        'usuario': 'George_Allison',
        'calificacion': '9.0 / 10',
        'foto_usuario': 'recursos/imagenes/usuarios/usuario_1.jpg',
        'titulo': 'BUENISIMA',
        'contenido': 'F1 es un espectáculo visual imponente que redefine el cine de automovilismo...',
        'likes': 100,
        'dislikes': 18,
        'comentarios_count': 50
    },
    {
        'usuario': 'Cinefilo88',
        'calificacion': '3.0 / 10',
        'foto_usuario': 'recursos/imagenes/usuarios/usuario_2.jpg',
        'titulo': 'REPETITIVA',
        'contenido': 'Aunque la acción es impecable, la banda sonora de Hans Zimmer se siente algo repetitiva...',
        'likes': 45,
        'dislikes': 12,
        'comentarios_count': 5
    }
]

def detalle_resenas_pelicula(request, pelicula_id):
    pelicula = {
        'id': pelicula_id,
        'titulo': 'F1 THE MOVIE',
        'imagen': 'recursos/imagenes/peliculas/f1.jpg',
        'anio': 2025,
        'duracion': '2h 35min',
        'puntuacion_promedio': 8.0,
        'total_opiniones': 4506
    }

    if request.method == 'POST':
        # Capturar la nueva reseña enviada por el formulario
        nueva_resena = {
            'usuario': request.POST.get('usuario', 'Usuario Anónimo'),
            'calificacion': f"{request.POST.get('calificacion', '10')} / 10",
            'foto_usuario': 'recursos/imagenes/usuarios/usuario_3.jpg', # Imagen por defecto
            'titulo': request.POST.get('titulo'),
            'contenido': request.POST.get('contenido'),
            'likes': 0,
            'dislikes': 0,
            'comentarios_count': 0
        }
        # Insertar al inicio de la lista
        RESENAS_LISTA.insert(0, nueva_resena)
        return redirect('peliculas:resenas_pelicula', pelicula_id=pelicula_id)
        

    contexto = {
        'pelicula': pelicula,
        'resenas': RESENAS_LISTA
    }
    return render(request, 'peliculas/resenas_usuarios.html', contexto)