from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import csv 
from django.conf import settings
from django.conf.urls.static import static

"""
Reads a csv file and returns a list 
"""
def read_cvs_to_list(file_name):

    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        listEstudiantes = list(reader)
    return listEstudiantes



