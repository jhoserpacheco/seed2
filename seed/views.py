from django.db.models.expressions import Subquery
from datetime import datetime, timedelta
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView, ListView, DetailView
from .forms import StudentCreateForm, TeacherCreateForm, GrupoCreateForm, ActividadCreateForm, TemaCreateForm

"""
IMPORT MODELS
"""
from .models import (
    Docente, 
    Estudiante,
    Grupo,
    Actividad, 
    Tema
)



from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={
        }
        return render(request, 'sign-with-google.html', context)
        
    def post(self, request, *args, **kwargs):
        print(self)
        if request.method == 'POST':
            form = StudentCreateForm(request.POST)
            print(form)
            if form.is_valid():
                email = form.cleaned_data['email']
                nombre = form.cleaned_data['nombre']
                url_img = form.cleaned_data['url_img'] 
                p, created = Estudiante.objects.get_or_create(email=email, nombre=nombre, url_img=url_img)
                p.save()
                form.save()
                return redirect('seed2:dashboardStudent')
        context={ 
        }
        return render(request, 'dashboard_student.html',context)

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        context = { 
        }
        return render(request, 'profileGoogle.html', context)



class CreateTeacherView(View):
    def get(self, request, *args, **kwargs):
        form = TeacherCreateForm()
        context = { 
            'form':form 
        }
        return render(request, 'created.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = TeacherCreateForm(request.POST)
            print(form)
            if form.is_valid():
                email = form.cleaned_data['email']
                nombre = form.cleaned_data['nombre']
                url_img = form.cleaned_data['url_img'] 
                p, created = Docente.objects.get_or_create(email=email, nombre=nombre, url_img=url_img)
                p.save()
                form.save()
                return redirect('seed2:create')
        context={ 
        }
        return render(request, 'docenteList.html',context)

class ListTeacherView(View):
    def get(self, request, *args, **kwargs):
        context = { 
            'docentes': Docente.objects.all()
        }
        return render(request, 'docenteList.html', context)

class CreateStudentView(View):
    
    def get(self, request, *args, **kwargs):
        form = StudentCreateForm()
        context = { 
            'form':form 
        }
        return render(request, 'profileGoogle.html', context)


class DashboardDocenteView(View):
    def get(self, request, *args, **kwargs):
        context = { 
            'grupos': Grupo.objects.all(),
            'actividades': Actividad.objects.all(),
            'temas': Tema.objects.all()
        }
        return render(request, 'Grupos/dashboard_docente.html', context)

"""
CRUD DE GRUPOS 
"""
class GrupoCreationView(View):
    def get(self, request, *args, **kwargs):
        form = GrupoCreateForm()
        context = { 
            'grupos': Grupo.objects.all(),
            'form':form 
        }
        return render(request, 'Grupos/grupoCreate.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = GrupoCreateForm(request.POST)
            print(form)
            if form.is_valid():
                codigo_grupo = form.cleaned_data['codigo_grupo']
                nombre = form.cleaned_data['nombre']
                docente = form.cleaned_data['docente'] 
                estado = form.cleaned_data['estado'] 
                p, created = Grupo.objects.get_or_create(codigo_grupo=codigo_grupo, nombre=nombre, docente=docente, estado=estado)
                p.save()
                form.save()
                return redirect('seed2:createGrupo')
        context={ 
        }
        return render(request, 'Grupos/dashboard_docente.html',context)

class GrupoDetailView(View):

    def get(self, request, codigo_grupo, *args, **kwargs):
        grupo = get_object_or_404(Grupo, codigo_grupo=codigo_grupo)
        tema = Tema.objects.filter(grupo_tema=codigo_grupo)
        actividad = Actividad.objects.filter(
            tema_actividad=Subquery(tema.values('codigo_tema'))
        )
        context = { 
            'grupo':grupo,
            'estudiantes': grupo.estudiante_set.values().all(),
            'temas': tema,
            'actividades': actividad

        }
        return render(request, 'Grupos/grupoDetalle.html',context)

class GrupoUpdateView(UpdateView):
    model = Grupo
    fields = ['codigo_grupo', 'nombre', 'docente', 'estado']
    template_name = 'Grupos/grupoDetalle.html'
    success_url = reverse_lazy('seed2:dashboardDocente')


class GrupoDeleteView(DeleteView):
    model = Grupo
    template_name = 'Grupos/grupoEliminar.html'
    success_url = reverse_lazy('seed2:dashboardDocente')

"""
CRUD DE ACTIVIDADES
"""

class ActividadCreationView(View):

    def get(self, request, *args, **kwargs):
        form = ActividadCreateForm()
        context = { 
            'form':form,
            'actividades': Actividad.objects.all(),
        }
        return render(request, 'Actividad/actividadCreate.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ActividadCreateForm(request.POST)
            print(form)
            #fields = {'codigo', 'nombre_ac', 'descripcion', 'estructura_de_datos', 'tema_actividad', 'fecha_inicio', 'fecha_fin', 'es_visible'}
            if form.is_valid():
                codigo = form.cleaned_data['codigo']
                nombre_ac = form.cleaned_data['nombre_ac']
                descripcion = form.cleaned_data['descripcion'] 
                estructura_de_datos = form.cleaned_data['estructura_de_datos'] 
                tema_actividad = form.cleaned_data['tema_actividad']
                fecha_inicio = form.cleaned_data['fecha_inicio']
                fecha_fin = form.cleaned_data['fecha_fin']
                es_visible = form.cleaned_data['es_visible']
                p, created = Actividad.objects.get_or_create(codigo=codigo, nombre_ac=nombre_ac, descripcion=descripcion, 
                    estructura_de_datos=estructura_de_datos,tema_actividad=tema_actividad, fecha_inicio=fecha_inicio, 
                    fecha_fin=fecha_fin, es_visible=es_visible)
                p.save()
                form.save()
                return redirect('seed2:createActividad')
        context={ 
        }
        return render(request, 'dashboard_docente.html',context)

class ActividadDetailView(View):

    def get(self, request, codigo, *args, **kwargs):
        actividad = get_object_or_404(Actividad, codigo=codigo)
        print(type(actividad.fecha_inicio))
        context = { 
            'actividad':actividad
        }
        return render(request, 'Actividad/actividadDetalle.html',context)

class ActividadUpdateView(UpdateView):
    model = Actividad
    fields = {'codigo', 'nombre_ac', 'descripcion', 'estructura_de_datos', 'tema_actividad', 'fecha_inicio', 'fecha_fin', 'es_visible'}
    template_name = 'Actividad/actividadDetalle.html'
    success_url = reverse_lazy('seed2:dashboardDocente')


class ActividadDeleteView(DeleteView):
    model = Actividad
    template_name = 'Actividad/actividadEliminar.html'
    success_url = reverse_lazy('seed2:dashboardDocente')


"""
CRUD DE TEMAS
"""
class TemaCreationView(View):
    def get(self, request, *args, **kwargs):
        form = TemaCreateForm()
        codigo_tema = request.GET.get('codigo_grupo')
        context = { 
            'temas': Tema.objects.all(),
            'form':form,
            'codigo_tema':codigo_tema
            
        }
        return render(request, 'Tema/temaCreate.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = TemaCreateForm(request.POST)
            print(form)
            #fields = {'codigo', 'nombre_ac', 'descripcion', 'estructura_de_datos', 'tema_actividad', 'fecha_inicio', 'fecha_fin', 'es_visible'}
            if form.is_valid():
                codigo_tema = form.cleaned_data['codigo_tema']
                nombre_tema = form.cleaned_data['nombre_tema']
                grupo_tema = form.cleaned_data['grupo_tema'] 
                p, created = Tema.objects.get_or_create(codigo_tema=codigo_tema, nombre_tema=nombre_tema, grupo_tema=grupo_tema)
                p.save()
                form.save()
                return redirect('seed2:createTema')
        context={ 
        }
        return render(request, 'Grupos/dashboard_docente.html',context)

class TemaDetailView(View):

    def get(self, request, codigo, *args, **kwargs):
        tema = get_object_or_404(Tema, codigo_tema=codigo)
        print(tema)
        context = { 
            'tema':tema
        }
        return render(request, 'Tema/temaDetalle.html', context)

class TemaUpdateView(UpdateView):
    model = Tema
    fields = fields = {'codigo_tema', 'nombre_tema', 'grupo_tema'}
    template_name = 'Tema/temaDetalle.html'
    success_url = reverse_lazy('seed2:dashboardDocente')


class TemaDeleteView(DeleteView):
    model = Tema
    template_name = 'Tema/temaEliminar.html'
    success_url = reverse_lazy('seed2:dashboardDocente')

class TemaActividadView(View):
    def get(self, request, pk,*args, **kwargs):
        actividad = Actividad.objects.filter(tema_actividad=pk)
        context={
            'actividades': actividad
        }
        return render(request, 'Tema/temaActividades.html', context)