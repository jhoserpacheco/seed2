
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.fields import DateTimeField
from django.utils.timezone import now


# Create your models here.
class Usuario(AbstractUser):
    url_img = models.CharField(
        max_length=250,
        default="", 
        blank=True
    )
    is_estudiante = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_docente = models.BooleanField(default=False)

    def get_estudiante(self):
        rol_estudiante = None
        if hasattr(self, 'estudiante'):
            rol_estudiante = self.estudiante
        return rol_estudiante

    def get_docente(self):
        rol_docente = None
        if hasattr(self, 'docente'):
            rol_docente = self.docente
        return rol_docente


    def __str__(self):
        return self.email


class Docente(models.Model):
    user = models.OneToOneField(Usuario,on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return '{} {} - {}'.format(self.user.first_name,self.user.last_name, self.user.username)

class Grupo(models.Model):
    codigo_grupo = models.CharField(
        primary_key=True,
        max_length=50
    )
    nombre = models.CharField(
        max_length=50,
        default="", 
    )
    docente = models.ForeignKey(
        Docente, 
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )
    estudiantes = models.FileField(
        upload_to='estudiantes/',
        null=True,
        blank=True
    )
 
    #temas = models.ForeignKey("Tema", on_delete=models.CASCADE, default="0000", null=True, blank=True)
    class Estado(models.TextChoices): 
        AC = 'AC', 'ACTIVO'
        IN = 'IN', 'INACTIVO'
        AR = 'AR', 'ARCHIVADO'
        
    estado = models.CharField(
        max_length = 9,
        choices = Estado.choices,
        default = Estado.AC
    )

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ['estado']
    
    def __str__(self):
        return self.codigo_grupo


class Estudiante(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    grupo = models.ForeignKey(Grupo, on_delete = models.CASCADE, default="", blank=True, null=True)
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return '{} {} - {}'.format(self.user.first_name,self.user.last_name, self.user.username)

class Tema(models.Model): 
    codigo_tema = models.IntegerField(primary_key=True, default="")
    nombre_tema = models.CharField(max_length=50, default="")
    grupo_tema = models.ForeignKey(Grupo, on_delete = models.CASCADE)
    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"
        ordering = ['nombre_tema']
    
    def __str__(self):
        return self.nombre_tema

class Actividad(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre_ac = models.CharField(max_length=50, verbose_name="Nombre de la actividad")
    descripcion = models.TextField(max_length=350)
    estudianteAct = models.ManyToManyField(Estudiante, through="Estudiante_Actividad")
    estructura_de_datos = models.ForeignKey(
        "EstructuraDeDatos", 
        on_delete=models.CASCADE, 
        default="0000"
    )
    tema_actividad = models.ForeignKey(
        Tema,
        on_delete = models.CASCADE, 
        default=""
    )
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    es_visible = models.BooleanField(default=True)

    def timeleft(self):
        nowt = now()
        fechaFin = self.fecha_fin
        restante = abs(fechaFin - nowt)
        stringLeft = str(restante.days) + " Dias, " + str(restante.seconds//3600)+ " Horas, "+str(restante.seconds//60%60)+ " Minutos, "+ str( restante.seconds%60) + " Segundos"
        if fechaFin < nowt:
            return stringLeft + " Atrasado"
        else:
            return stringLeft + " Restante"
        
    def getFechaInicio(self):
        return self.fecha_inicio.strftime("%Y-%m-%d %I:%M:%S")

    def getFechaFin(self):
        return self.fecha_fin.strftime("%Y-%m-%d %I:%M:%S")
    
    def getNow(self):
        return now().strftime("%Y-%m-%d %I:%M:%S")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ['nombre_ac']

    def __str__(self):
        return self.nombre_ac

class Estudiante_Actividad(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete = models.CASCADE)
    activity = models.ForeignKey(Actividad, on_delete = models.CASCADE)
    class Estado(models.TextChoices): 
        P = 'P', 'PENDIENTE'
        C = 'C', 'CALIFICADA'

    estado = models.CharField(
        max_length = 2,
        choices = Estado.choices,
        default = Estado.P
    )
    nota = models.FloatField(default=0.0)
    comentario = models.TextField(max_length=500, default="No hay comentarios.")
    fecha_entrega = models.DateTimeField(default=now, blank=True)
    class Meta:
        verbose_name = "Estudiante_Actividad"
        verbose_name_plural = "Estudiantes_Actividades"
        ordering = ['estado']

    def __str__(self):
        return str(self.activity) +' - '+ str(self.estudiante) 

    def getNow(self):
        return now().strftime("%Y-%m-%d %I:%M:%S")

class EstructuraDeDatos(models.Model):
    codigo_ed = models.IntegerField(primary_key=True)
    nombre_ed = models.CharField(max_length=50)
    #actividad = models.OneToOneField(Actividad, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre_ed



