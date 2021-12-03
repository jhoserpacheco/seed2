from django.http import JsonResponse
from .models import Grupo

def eliminar_identificador(request):
    print("eliminar_identificador............",request)
    pk = request.GET.get('identificador_id')
    identificador = Grupo.objects.get(pk=pk)
    identificador.delete()
    response = {}
    return JsonResponse(response)