from django import forms
from allauth.socialaccount.models import SocialAccount
from .models import Estudiante, Docente

class TeacherCreate(forms.ModelForm):
    class Meta:
        model = Docente
        fields =  ('email', 'nombre', 'url_img')
        widgets = {'email': forms.HiddenInput(), 'nombre': forms.HiddenInput(), 'url_img': forms.HiddenInput()}
        #initial = {'email': SocialAccount.get_deferred_fields, 'nombre': SocialAccount.get_profile_url, 'url_img': SocialAccount.get_avatar_url}
