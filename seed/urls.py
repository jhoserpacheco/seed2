from django.urls.resolvers import URLPattern
from django.urls import path, include 
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('main/', views.main, name='main'),
    path('', include('main.urls')), 

]