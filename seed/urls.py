from django.conf.urls import url
from django.urls.resolvers import URLPattern
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import *
from .ajax import *

app_name = 'seed2'

urlpatterns = [
    path('',logi.as_view(), name='login'),
    path('logout/',logou.as_view(), name='logout'),
    #path('loging/', loging.as_view(), name='loging'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('create/', CreateTeacherView.as_view(), name='create'),
    path('list/', ListTeacherView.as_view(), name='list'),
    path('dashboardEstudiante/', DashboardStudentView.as_view(), name='dashboardStudent'),
    path('dashboardDocente/',DashboardDocenteView.as_view(), name='dashboardDocente'),
    path('dashboardEstudiante/actividad/<pk>', SubirActividadEstudianteView.as_view(), name='uploadActividad'),
    ## Grupos
    path('dashboardDocente/grupos/create', GrupoCreationView.as_view(), name='createGrupo'),
    path('dashboardDocente/grupos/<codigo_grupo>/', GrupoDetailView.as_view(), name='detailGrupo'),
    path('dashboardDocente/grupos/<pk>/update/', GrupoUpdateView.as_view(), name='updateGrupo'),
    path('dashboardDocente/grupos/<pk>/delete/', GrupoDeleteView.as_view(), name='deleteGrupo'),
    url(r'eliminar_grupo/$', eliminar_grupo, name='eliminar_grupo'),#url de ajax para eliminar identificador(grupo)
    url(r'eliminar_tema/$', eliminar_tema, name='eliminar_tema'),#url de ajax para eliminar identificador(tema)
    url(r'eliminar_actividad/$', eliminar_actividad, name='eliminar_actividad'),#url de ajax para eliminar identificador(actividad)

    ## Actividad
    path('dashboardDocente/actividad/create', ActividadCreationView.as_view(), name='createActividad'),
    path('dashboardDocente/actividad/<int:codigo>/', ActividadDetailView.as_view(), name='detailActividad'),
    path('dashboardDocente/actividad/<pk>/update/', ActividadUpdateView.as_view(), name='updateActividad'),
    path('dashboardDocente/actividad/<pk>/delete/', ActividadDeleteView.as_view(), name='deleteActividad'),
    path('dashboardDocente/calificarActividad/<actividad>/<estudiante>/' , CalificarActividadView.as_view(), name='calificarActividad'),

    ## Tema
    path('dashboardDocente/tema/create', TemaCreationView.as_view(), name='createTema'),
    path('dashboardDocente/tema/<int:codigo>/', TemaDetailView.as_view(), name='detailTema'),
    path('dashboardDocente/tema/<pk>/update/', TemaUpdateView.as_view(), name='updateTema'),
    path('dashboardDocente/tema/<pk>/delete/', TemaDeleteView.as_view(), name='deleteTema'), 
    path('dashboardDocente/tema/<pk>/actividades/', TemaActividadView.as_view(), name='temaActividades'), 
    
    
]