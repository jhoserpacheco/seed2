from django.contrib import admin

# Register your models here.

from .models import Docente, Grupo, Estudiante

admin.site.register(Docente)
admin.site.register(Grupo)
admin.site.register(Estudiante)