from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.

class Usuario(AbstractUser):
    url_img = models.CharField(
        max_length=250,
        default="", 
        blank=True
    )
    es_admin = models.BooleanField(default=False)
    es_docente = models.BooleanField(default=False)
    is_estudiante = models.BooleanField(default=False)

    def __str__(self):
        return self.email



class Estudiante(models.Model):
    user = models.OneToOneField(Usuario,on_delete=models.CASCADE ,primary_key=True)
    grupo = models.ForeignKey('Grupo', on_delete = models.DO_NOTHING, default="", blank=True, null=True)
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return '{} {} - {}'.format(self.user.first_name,self.user.last_name, self.user.username)


class Docente(models.Model):
    user = models.OneToOneField(Usuario,on_delete=models.CASCADE, primary_key=True)

