from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic import FormView
from django.views.generic import TemplateView

from grace.members_area.forms import LoginForm, RegisterForm


class MembersView(TemplateView):

    template_name = 'members_area/members_area_form.html'

    def get(self, request, *args, **kwargs):
        login_form = LoginForm(self.request.GET or None)
        register_form = RegisterForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['login_form'] = login_form
        context['register_form'] = register_form
        return self.render_to_response(context)


class LoginFormView(FormView):

    form_class = LoginForm
    template_name = 'members_area/members_area_form.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        login_form = self.form_class(request.POST)
        register_form = RegisterForm()
        if login_form.is_valid():
            return HttpResponseRedirect('/membros/')
        else:
            return self.render_to_response(self.get_context_data(login_form=login_form, register_form=register_form))


class RegisterFormView(FormView):

    form_class = RegisterForm
    template_name = 'members_area/members_area_form.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):

        register_form = self.form_class(request.POST)
        login_form = LoginForm()

        if register_form.is_valid():
            body = render_to_string('members_area/register_email.txt', register_form.cleaned_data)
            mail.send_mail('Confirmação de registro',
                           body,
                           'contato@elitedev.com.br',
                           ['contato@elitedev.com.br', register_form.cleaned_data['email']])
            messages.success(request, 'Registro realizado com sucesso!')
            return HttpResponseRedirect('/membros/')
        else:
            return self.render_to_response(self.get_context_data(register_form=register_form, login_form=login_form))
