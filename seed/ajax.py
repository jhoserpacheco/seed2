from django.http import JsonResponse
from .models import *

def eliminar_grupo(request):
    identificador = Grupo.objects.get(pk=pk)
    identificador.delete()
    response = {}
    return JsonResponse(response)

def eliminar_tema(request):
    pk = request.GET.get('identificador_id')
    identificador = Tema.objects.get(pk=pk)
    identificador.delete()
    response = {}
    return JsonResponse(response)

def eliminar_actividad(request):
    pk = request.GET.get('identificador_id')
    identificador = Actividad.objects.get(pk=pk)
    identificador.delete()
    response = {}
    return JsonResponse(response)