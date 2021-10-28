from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView
from .forms import TeacherCreate 
from .models import Docente
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={
        }
        return render(request, 'sign-with-google.html', context)

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        context = { 
        }
        return render(request, 'profileGoogle.html', context)


class CreateTeacherView(View):
    def get(self, request, *args, **kwargs):
        form = TeacherCreate()
        context = { 
             'form':form 
        }
        return render(request, 'created.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = TeacherCreate(request.POST)
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

