from django.shortcuts import render
from django.http import HttpResponse
from webserviceapp.models import tComentarios, tPeliculas
from django.views.decorators.csrf import csrf_exempt
import json

def pagina_de_prueba(request):
			return HttpResponse("<h1>Hola caracola</h1>");

def devolver_peliculas(request):
			peliculas = tPeliculas.objects.all();
			respuesta_final = []
			for fila_sql in peliculas:
			diccionario = {}
			diccionario['id'] = fila_sql.id
			diccionario['nombre'] = fila_sql.nombre
			diccionario['genero'] = fila_sql.genero
			diccionario['categoria'] = fila_sql.categoria
			diccionario['url_imagen'] = fila_sql.url_image
			respuesta_final.append(diccionario)
return JsonResponse(respuesta_final, safe=False)

def devolver_pelicula_por_id(request, id_solicitado):
		peliculas = tPeliculas.objects.get(id=id_solicitado)
		comentarios = peliculas.tComentarios_set.all()
		lista_comentarios = []

		for fila_comentario_sql in  comentarios:
			diccionario = {}
			diccionario['id'] = fila_comentario_sql.id
			diccionario['comentario'] = fila_comenatario_sql.comentario
			lista_comentarios.append(diccionario)
		resultado = {

			'id': peliculas.id,
			'nombre': peliculas.nombre,
			'url_image': peliculas.url_image,
			'genero': peliculas.genero,
			'categoria': peliculas.categoria


}

return JsonResponse(resultado, json_dumps_params={'ensure_ascii':False})

@csrf_exempt
def guardar_comentario(request, id_solicitado):
			if request.method != 'POST':
				return None

			json_peticion = json.loads(request.body)

			nuevo_comentario = tComentarios()
			nuevo_comentario.comentarios = json_peticion['nuevo_comentario']
			nuevo_comentario.cancion = tPeliculas.objects.get(id=id_solicitado)
			nuevo_comentario.save()
			return JsonResponse({"status": "ok"})


