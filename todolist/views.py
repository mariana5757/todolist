from django.shortcuts import render
from django.http import JsonResponse
from .models import Tareas
from django.views.decorators.csrf import csrf_exempt
from corsheaders.defaults import default_headers

import json

# Create your views here.
def leer(request):
    tareas = Tareas.objects.values()
    list_tareas = list(tareas)
    return JsonResponse({'lista' : list_tareas})

@csrf_exempt
def guardar(request):
    print(request)
    if (request.method == 'POST'):
        data = json.loads(request.body)
        Tareas.objects.create(tarea = data['tarea'])
        return JsonResponse({'mensaje' : "datos recibidos con éxito"})
    return JsonResponse({'mensaje' : 'no ha guardado nada'})

@csrf_exempt
def modificar(request, id = 2):
    print("entra")
    if (request.method == 'PUT'):
        tarea = Tareas.objects.filter(id = id).first()
        if tarea:
            data = "tarea nueva"
            tarea.tarea = data
            tarea.save()
            return JsonResponse({'mensaje' : 'Actualizado'})
        return JsonResponse({'mensaje' : 'no exite la tarea'})
    return JsonResponse({'mensaje' : 'No es método post'})

@csrf_exempt
def eliminar(request, id = 2):
    if (request.method == 'DELETE'):
        tarea = Tareas.objects.filter(id = id).first()
        if tarea:
            tarea.delete()
            return JsonResponse({'mensaje' : 'Eliminada'})
        return JsonResponse({'mensaje' : 'no exite la tarea'})
    return JsonResponse({'mensaje' : 'No es método post'})