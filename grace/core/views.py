from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from grace.core.forms import HomeContactForm


def home(request):

    if request.method == 'POST':
        return create_form_contact(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'index.html', {'form': HomeContactForm()})


def create_form_contact(request):

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

    #Success
    messages.success(request, 'E-mail enviado com sucesso!')
    return HttpResponseRedirect('/#contact')


def _send_contact_mail(subject, from_, to, template_email_name, context):
    body = render_to_string(template_email_name, context)
    mail.send_mail(subject, body, from_, to)