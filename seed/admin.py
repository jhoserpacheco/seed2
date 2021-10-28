from django.contrib import admin

# Register your models here.

from .models import Docente, Grupo, Estudiante, Actividad, Tema

admin.site.register(Docente)
admin.site.register(Grupo)
admin.site.register(Estudiante)
admin.site.register(Actividad)
admin.site.register(Tema)
