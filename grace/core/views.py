from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from grace.core.forms import HomeContactForm

# Create your views here.

def home(request):

    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):

    form = HomeContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'index.html', {'form': form})

    form.full_clean()

    #Send email
    _send_contact_mail('Requisição de contato Grace ERP',
                       form.cleaned_data['ur_email'],
                       ['contato@elitedev.com.br'],
                       'contact_email.txt',
                       form.cleaned_data)
    return HttpResponseRedirect('/')


def new(request):
    return render(request, 'index.html', {'form': HomeContactForm()})


def _send_contact_mail(subject, from_, to, template_email_name, context):
    body = render_to_string(template_email_name, context)
    mail.send_mail(subject, body, from_, to)