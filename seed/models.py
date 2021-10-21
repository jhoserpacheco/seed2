from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Docente(models.Model):
    email = models.EmailField(primary_key=True, null=False, unique=True)
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    def __str__(self):
        return self.email

class Grupo(models.Model):
    codigo_grupo = models.CharField(max_length=50, primary_key=True)
    docente = models.ForeignKey(Docente, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.codigo_grupo

class Estudiante(models.Model):
    email = models.EmailField(primary_key=True, null=False, unique=True)
    grupo = models.ForeignKey(Grupo, on_delete = models.DO_NOTHING, default="")
    nombre_estudiante = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.email
