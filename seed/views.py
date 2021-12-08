from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.expressions import Subquery
from django.http.response import FileResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from seed.decorators import docente_required, estudiante_required

from utils.readcsv import read_cvs_to_list

"""
IMPORT FORMS
"""
from .forms import StudentCreateForm, TeacherCreateForm, GrupoCreateForm, ActividadCreateForm, TemaCreateForm, ActividadEstudianteForm

"""
IMPORT MODELS
"""
from .models import (
    Docente, 
    Estudiante,
    Grupo,
    Actividad, 
    Tema,
    Usuario, 
    Estudiante_Actividad
)



from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
import os
from django.conf import settings

# Create your views here.

def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.is_docente:
        return redirect('seed2:dashboardDocente')
    elif request.user.is_estudiante:
        return redirect('seed2:dashboardStudent')
    else:
        return redirect('seed2:login')


#login de django
class logou(View): 
    
    def get(self, request, *args, **kwargs):
        context={}
        logout(request)
        return render(request, 'Cuenta/login.html', context)
        

class logi(View):
    def get(self, request, *args, **kwargs):
        print("...validando template...")
        context={}
        return render(request, 'Cuenta/login.html', context)
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("...validando post user...")
            username = request.POST['useremail']
            password = request.POST['userpassword']
            user = authenticate(username=username, password=password)
            """if user is not None:
                login(request, user)
                if user.is_docente:
                    print("userrrrrrrrrrrrrrrrr", request.user.is_docente)
                return redirect('seed2:dashboardDocente')
            else:
                return redirect('seed2:login')
                """
    def redirect(self, request, *args, **kwargs):
        print("...validando direccionamiento...")
        if request.use is None:
            if request.user.is_docente:
                pass
                #return redirect('seed2:dashboardDocente')
            else:
                return redirect('seed2:dashboardEstudiante')
        else:
            return redirect('seed2:login')

class loging(View):
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



@method_decorator([login_required], name='dispatch')
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
                user = form.cleaned_data['user']
                p, created = Docente.objects.get_or_create(user=user)
                p.save()
                form.save()
                return redirect('seed2:create')
        context={ 
        }
        return render(request, 'docenteList.html',context)

@method_decorator([login_required], name='dispatch')
class ListTeacherView(View):
    def get(self, request, *args, **kwargs):
        context = { 
            'docentes': Docente.objects.all()
        }
        return render(request, 'docenteList.html', context)

@method_decorator([login_required], name='dispatch')
class CreateStudentView(View):
    
    def get(self, request, *args, **kwargs):
        form = StudentCreateForm()
        context = { 
            'form':form 
        }
        return render(request, 'profileGoogle.html', context)

@method_decorator([login_required, docente_required], name='dispatch')
class DashboardDocenteView(View):
    def get(self, request, *args, **kwargs):
        context = { 
            'grupos': Grupo.objects.all(),
            'actividades': Actividad.objects.all(),
            'temas': Tema.objects.all()
        }
        return render(request, 'Grupos/dashboard_docente.html', context)
@method_decorator([login_required, estudiante_required], name='dispatch')
class DashboardStudentView(View):
    def get(self, request, *args, **kwargs):
        grupos = Grupo.objects.filter(codigo_grupo=request.user.get_estudiante().grupo.codigo_grupo).all()
        tema = Tema.objects.filter(grupo_tema=request.user.get_estudiante().grupo.codigo_grupo)
        actividad = Actividad.objects.filter(tema_actividad=Subquery(tema.values('codigo_tema')))
        context = { 
            'grupos': grupos,
            'temas': tema, 
            'actividades': actividad
        }
        return render(request, 'Grupos/dashboard_estudiante.html', context)

"""
Estudiante subir actividad
"""
class SubirActividadEstudianteView(View):
    def get(self, request, pk,*args, **kwargs):
        form = ActividadEstudianteForm()
        actividad = Actividad.objects.filter(codigo=pk).first()
        context = { 
            'actividad': actividad,
            'now': actividad.getNow(),
            'form':form, 
            'actividadSubida': self.validarEntrega(actividad.codigo, request.user.get_estudiante().user.id, request)
        }
        return render(request, 'Actividad/estudianteActividad.html', context)

    def post(self, request, pk, *args, **kwargs):
        if request.method == 'POST':
            form = ActividadEstudianteForm(request.POST, request.FILES)

            print(form)
            if form.is_valid() and not self.validarEntrega(pk, request.user.get_estudiante().user.id, request):
                estudiante = form.cleaned_data['estudiante']
                activity = form.cleaned_data['activity']
                estado = form.cleaned_data['estado']
                nota = form.cleaned_data['nota'] 
                comentario = form.cleaned_data['comentario'] 
                fecha_entrega = form.cleaned_data['fecha_entrega'] 
                entregaFile = form.cleaned_data['entregaFile']
                
                p, created = Estudiante_Actividad.objects.get_or_create(estudiante=estudiante, activity=activity, estado=estado,
                                                            nota=nota, comentario=comentario, fecha_entrega=fecha_entrega, entregaFile=entregaFile)
                p.save()
                return redirect('seed2:dashboardStudent')
        context={ 
            
        }
        return render(request, 'Grupos/dashboard_estudiante.html',context)

    def validarEntrega(self, pk, e, request, *args, **kwargs):
        actividad = Actividad.objects.filter(codigo=pk, estudianteAct = e).first()
        ae = Estudiante_Actividad.objects.filter(activity=actividad, estudiante=e).all()
        print(pk)
        return len(ae) > 0
        



"""
CRUD DE GRUPOS 
"""

@method_decorator([login_required, docente_required], name='dispatch')
class GrupoCreationView(View):
    def get(self, request, *args, **kwargs):
        form = GrupoCreateForm()
        context = { 
            'grupos': Grupo.objects.filter(docente=request.user.id).all(),
            'soy':request.user,
            'form':form 
        }
        return render(request, 'Grupos/grupoCreate.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = GrupoCreateForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                estudiantes = form.cleaned_data['estudiantes']
                codigo_grupo = form.cleaned_data['codigo_grupo']
                nombre = form.cleaned_data['nombre']
                docente = form.cleaned_data['docente'] 
                estado = form.cleaned_data['estado'] 
                p, created = Grupo.objects.get_or_create(codigo_grupo=codigo_grupo, nombre=nombre, docente=docente, estado=estado, estudiantes=estudiantes)
                GrupoCreationView.setUserToStudent(p)
                p.save()
                form.save()
                return redirect('seed2:createGrupo')
        context={ 
            
        }
        return render(request, 'Grupos/dashboard_docente.html',context)

    """
        METODO PARA ASIGNAR UN ESTUDIANTE A UN GRUPO 
    """
    def setUserToStudent(grupo):
        if grupo.estudiantes.name != None:
            rutaCSV =  'media/' + grupo.estudiantes.name
            print('ruta',rutaCSV)
            correos = read_cvs_to_list(rutaCSV)
            for estudiante in correos:
                print(estudiante[0])
                student = Estudiante()
                email = str(estudiante[0])
                try:
                    user = Usuario.objects.get(email=email)
                    student.user = user
                    student.grupo = Grupo.objects.get(codigo_grupo=grupo.codigo_grupo)
                    user.is_estudiante = True
                    user.save()
                    student.save()
                except: 
                    pass
                


@method_decorator([login_required, docente_required], name='dispatch')
class GrupoDetailView(View):

    def get(self, request, codigo_grupo, *args, **kwargs):
        grupo = get_object_or_404(Grupo, codigo_grupo=codigo_grupo)
        tema = Tema.objects.filter(grupo_tema=codigo_grupo)
        actividad = Actividad.objects.filter(
            tema_actividad=Subquery(tema.values('codigo_tema'))
        )
        context = { 
            'grupo':grupo,
            'estudiantes': grupo.estudiante_set.all(),
            'temas': tema,
            'actividades': actividad

        }
        return render(request, 'Grupos/grupoDetalle.html',context)

@method_decorator([login_required], name='dispatch')
class GrupoUpdateView(UpdateView):
    model = Grupo
    fields = ['codigo_grupo', 'nombre', 'docente', 'estado']
    template_name = 'Grupos/grupoDetalle.html'
    success_url = reverse_lazy('seed2:dashboardDocente')


@method_decorator([login_required], name='dispatch')
class GrupoDeleteView(DeleteView):
    model = Grupo
   
    
    template_name = 'Grupos/grupoEliminar.html'
    success_url = reverse_lazy('seed2:dashboardDocente')

"""
CRUD DE ACTIVIDADES
"""

@method_decorator([login_required], name='dispatch')
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

@method_decorator([login_required, docente_required], name='dispatch')
class ActividadDetailView(View):

    def get(self, request, codigo, *args, **kwargs):
        actividad = get_object_or_404(Actividad, codigo=codigo)
        actividadEstudiante = Estudiante_Actividad.objects.filter(activity=codigo).all()
        context = { 
            'actividad': actividad,
            'entregaActividad' : actividadEstudiante,
            'form': ActividadCreateForm()
        }
        return render(request, 'Actividad/actividadDetalle.html',context)

@method_decorator([login_required, docente_required], name='dispatch')
class ActividadUpdateView(UpdateView):
    model = Actividad
    fields = {'codigo', 'nombre_ac', 'descripcion', 'estructura_de_datos', 'tema_actividad', 'fecha_inicio', 'fecha_fin', 'es_visible'}
    template_name = 'Actividad/actividadDetalle.html'
    success_url = reverse_lazy('seed2:dashboardDocente')


@method_decorator([login_required, docente_required], name='dispatch')
class ActividadDeleteView(DeleteView):
    model = Actividad
    template_name = 'Actividad/actividadEliminar.html'
    success_url = reverse_lazy('seed2:dashboardDocente')

@method_decorator([login_required, docente_required], name='dispatch')
class CalificarActividadView(View): 
    def get(self, request, actividad, estudiante, *args, **kwargs):
        actividadEstudiante = Estudiante_Actividad.objects.filter(activity=actividad, estudiante=estudiante).first()
        form = ActividadEstudianteForm()
        context = { 
            'form':form,
            'entregaActividad' : actividadEstudiante,
        }
        return render(request, 'Actividad/calificarActividad.html',context)
    
    def post(self, request, actividad, estudiante, *args, **kwargs):
        actividadEstudiante = Estudiante_Actividad.objects.get(activity=actividad, estudiante=estudiante)
        form = ActividadEstudianteForm(request.POST)
        if form.is_valid():
            actividadEstudiante.nota = form.cleaned_data['nota']
            actividadEstudiante.comentario = form.cleaned_data['comentario']
            actividadEstudiante.estado = "C"
            actividadEstudiante.save()
            return redirect('seed2:detailActividad', actividad)
        context={ 
        }
        return render(request, 'Grupos/dashboard_docente.html',context)


"""
CRUD DE TEMAS
"""
@method_decorator([login_required], name='dispatch')
class TemaCreationView(View):
    def get(self, request, *args, **kwargs):
        form = TemaCreateForm()
        codigo_tema = request.GET.get('codigo_grupo')
        tema = Tema.objects.all()
        context = { 
            'temas': tema,
            'form':form,
            'codigo_tema':codigo_tema, 
            
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
                estado = 'C'
                p, created = Tema.objects.get_or_create(codigo_tema=codigo_tema, nombre_tema=nombre_tema, grupo_tema=grupo_tema, estado=estado)
                p.save()
                form.save()
                return redirect('seed2:createTema')
        context={ 
        }
        return render(request, 'Grupos/dashboard_docente.html',context)

@method_decorator([login_required], name='dispatch')
class TemaDetailView(View):

    def get(self, request, codigo, *args, **kwargs):
        tema = get_object_or_404(Tema, codigo_tema=codigo)
        codigo_tema = tema.codigo_tema
        context={
            'tema':tema,
            'codigo_tema':codigo_tema,
        }
        return render(request, 'Tema/temaDetalle.html', context)

@method_decorator([login_required], name='dispatch')
class TemaUpdateView(UpdateView):
    model = Tema
    fields = fields = {'codigo_tema', 'nombre_tema', 'grupo_tema'}
    template_name = 'Tema/temaDetalle.html'
    success_url = reverse_lazy('seed2:dashboardDocente')

    def get(self, request, pk, *args, **kwargs):
        tema = get_object_or_404(Tema, codigo_tema=pk)
        actividades = Actividad.objects.filter(tema_actividad=pk)
        context={
            'tema':tema,
            'actividades':actividades,
        }
        return render(request, 'Tema/temaDetalle.html', context)


@method_decorator([login_required], name='dispatch')
class TemaDeleteView(DeleteView):
    model = Tema
    template_name = 'Tema/temaEliminar.html'
    success_url = reverse_lazy('seed2:dashboardDocente')

@method_decorator([login_required], name='dispatch')
class TemaActividadView(View):
    def get(self, request, pk,*args, **kwargs):
        actividad = Actividad.objects.filter(tema_actividad=pk)
        context={
            'actividades': actividad
        }
        return render(request, 'Tema/temaActividades.html', context)


"""
CRUD DE ESTUDIANTE ACTIVIDAD
"""
