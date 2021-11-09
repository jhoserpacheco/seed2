from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import csv 

def read_cvs_to_list(file_name):
    """
    Reads a csv file and returns a list of lists.
    """
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        print(list(reader))



def send_email(request):
    """
    Sends an email to the specified email address.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        try:
            send_mail(subject, message, ' ', [email])    
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/success')
    