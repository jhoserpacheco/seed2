from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView
# Create your views here.

def main(request):
    return HttpResponse("Successfully logged in!")