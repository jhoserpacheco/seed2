from django.contrib import admin

# Register your models here.

from .models import Docente, Grupo, Estudiante, Actividad, Tema, Estudiante_Actividad, EstructuraDeDatos
from usuarios.models import  Estudiante, Docente

admin.site.register(Docente)
admin.site.register(Grupo)
admin.site.register(Estudiante)
admin.site.register(Actividad)
admin.site.register(Tema)
admin.site.register(Estudiante_Actividad)
admin.site.register(EstructuraDeDatos)


