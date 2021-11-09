from django import forms
from allauth.socialaccount.models import SocialAccount
from .models import Estudiante, Docente, Grupo, Actividad, Tema

class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields =  ('email', 'nombre', 'url_img')
        widgets = {'email': forms.HiddenInput(), 'nombre': forms.HiddenInput(), 'url_img': forms.HiddenInput()}
        #initial = {'email': SocialAccount.get_deferred_fields, 'nombre': SocialAccount.get_profile_url, 'url_img': SocialAccount.get_avatar_url}

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields =  ('email', 'nombre', 'url_img')
        widgets = {'email': forms.HiddenInput(), 'nombre': forms.HiddenInput(), 'url_img': forms.HiddenInput()}
        #initial = {'email': SocialAccount.get_deferred_fields, 'nombre': SocialAccount.get_profile_url, 'url_img': SocialAccount.get_avatar_url}

class GrupoCreateForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = {'codigo_grupo', 'nombre', 'docente', 'estado'}

class ActividadCreateForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Actividad
        fields = {'codigo', 'nombre_ac', 'descripcion', 'estructura_de_datos', 'tema_actividad', 'fecha_inicio', 'fecha_fin', 'es_visible'}
        format = {'fecha_inicio': '%d/%m/%Y', 'fecha_fin': '%d/%m/%Y'}

class TemaCreateForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = {'codigo_tema', 'nombre_tema', 'grupo_tema'}
        








