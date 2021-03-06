from django import forms
from allauth.socialaccount.models import SocialAccount
from django.core.files.base import File
from django.db.models import fields
from django.forms.widgets import DateTimeInput, Select
from .models import Estudiante, Docente, Grupo, Actividad, Tema, Estudiante_Actividad

class TeacherCreateForm(forms.ModelForm):
    is_docente = forms.BooleanField(widget=forms.RadioSelect(choices=((True, 'Si'), (False, 'No'))))
    class Meta:
        model = Docente
        fields = '__all__'

class StudentCreateForm(forms.ModelForm):
    pass
 #   class Meta:
  #      model = Estudiante
   ##     fields =  ('email', 'nombre', 'url_img')
    #    widgets = {'email': forms.HiddenInput(), 'nombre': forms.HiddenInput(), 'url_img': forms.HiddenInput()}
        #initial = {'email': SocialAccount.get_deferred_fields, 'nombre': SocialAccount.get_profile_url, 'url_img': SocialAccount.get_avatar_url}

class GrupoCreateForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = {'codigo_grupo', 'nombre', 'docente', 'estado', 'estudiantes'}

class ActividadCreateForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    fecha_fin = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Actividad
        fields = {'codigo', 'nombre_ac', 'descripcion', 'estructura_de_datos', 'tema_actividad', 'fecha_inicio', 'fecha_fin', 'es_visible'}
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }
        format = {
            'fecha_inicio': DateTimeInput(attrs={'type': 'datetime-local', 'timezone': 'America/Bogota'}),
            'fecha_fin': DateTimeInput(attrs={'type': 'datetime-local', 'timezone': 'America/Bogota'}),
            'es_visible': 'RadioSelect'
            }


class TemaCreateForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = {'codigo_tema', 'nombre_tema', 'grupo_tema'}

class ActividadEstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante_Actividad
        fields = {'estudiante', 'activity', 'estado', 'nota', 'comentario', 'fecha_entrega', 'entregaFile'}
        format = {'fecha_entrega': DateTimeInput(attrs={'type': 'datetime-local', 'timezone': 'America/Bogota'},),}
        
        








