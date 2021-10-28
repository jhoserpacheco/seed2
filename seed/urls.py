from django.conf.urls import url
from django.urls.resolvers import URLPattern
from django.urls import path, include
from .views import HomeView, ProfileView, CreateTeacherView, ListTeacherView
from django.views.generic import TemplateView

app_name = 'seed2'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('create/', CreateTeacherView.as_view(), name='create'),
    path('list/', ListTeacherView.as_view(), name='list'),
]