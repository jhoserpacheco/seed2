from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import csv 

"""
Reads a csv file and returns a list of lists.
"""
def read_cvs_to_list(file_name):

    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        listEstudiantes = list(reader)
    return listEstudiantes

print(read_cvs_to_list('../media/emails.csv'))

