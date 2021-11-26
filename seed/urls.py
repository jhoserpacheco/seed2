from django.conf.urls import url
from django.urls.resolvers import URLPattern
from django.urls import path, include, re_path
from .views import *
from django.views.generic import TemplateView

app_name = 'seed2'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('create/', CreateTeacherView.as_view(), name='create'),
    path('list/', ListTeacherView.as_view(), name='list'),
    path('dashboardStudent/', CreateStudentView.as_view(), name='dashboardStudent'),
    path('dashboardDocente/', DashboardDocenteView.as_view(), name='dashboardDocente'),
    ## Grupos
    path('dashboardDocente/grupos/create', GrupoCreationView.as_view(), name='createGrupo'),
    path('dashboardDocente/grupos/<codigo_grupo>/', GrupoDetailView.as_view(), name='detailGrupo'),
    path('dashboardDocente/grupos/<pk>/update/', GrupoUpdateView.as_view(), name='updateGrupo'),
    path('dashboardDocente/grupos/<pk>/delete/', GrupoDeleteView.as_view(), name='deleteGrupo'),

    ## Activdad
    path('dashboardDocente/actividad/create', ActividadCreationView.as_view(), name='createActividad'),
    path('dashboardDocente/actividad/<int:codigo>/', ActividadDetailView.as_view(), name='detailActividad'),
    path('dashboardDocente/actividad/<pk>/update/', ActividadUpdateView.as_view(), name='updateActividad'),
    path('dashboardDocente/actividad/<pk>/delete/', ActividadDeleteView.as_view(), name='deleteActividad'),

    ## Tema
    path('dashboardDocente/tema/create', TemaCreationView.as_view(), name='createTema'),
    path('dashboardDocente/tema/<int:codigo>/', TemaDetailView.as_view(), name='detailTema'),
    path('dashboardDocente/tema/<pk>/update/', TemaUpdateView.as_view(), name='updateTema'),
    path('dashboardDocente/tema/<pk>/delete/', TemaDeleteView.as_view(), name='deleteTema'), 
    path('dashboardDocente/tema/<pk>/actividades/', TemaActividadView.as_view(), name='temaActividades'), 
    
    
]