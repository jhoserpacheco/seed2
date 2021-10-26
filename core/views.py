from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={
        }
        return render(request, 'sign-with-google.html', context)

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        context={
        }
        return render(request, 'profileGoogle.html', context)