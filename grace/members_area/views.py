from django.conf import settings
from django.core import mail
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.shortcuts import resolve_url as r


from grace.members_area.forms import LoginForm, RegisterForm
from grace.members_area.models import Registration


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

    def post(self, request, *args, **kwargs):
        login_form = self.form_class(request.POST)
        register_form = RegisterForm()

        if not login_form.is_valid():
            return self.render_to_response(self.get_context_data(login_form=login_form, register_form=register_form))

        return HttpResponseRedirect(r('members:login'))


class RegisterFormView(FormView):

    form_class = RegisterForm
    template_name = 'members_area/members_area_form.html'

    def post(self, request, *args, **kwargs):

        register_form = self.form_class(request.POST)
        login_form = LoginForm()

        if not register_form.is_valid():
            return self.render_to_response(self.get_context_data(register_form=register_form, login_form=login_form))

        registration = register_form.save()

        # Send email
        _send_register_mail('Confirmação de registro',
                            settings.DEFAULT_FROM_EMAIL,
                            registration.email,
                            'members_area/register_email.txt',
                            {'registration': registration})

        return HttpResponseRedirect(r('members:success', str(registration.hashId)))


def detail(request, hashid):

    try:
        registration = Registration.objects.get(hashId=hashid)
    except Registration.DoesNotExist:
        raise Http404

    return render(request, 'members_area/members_area_success.html', {'registration': registration})


def _send_register_mail(subject, from_, to, template_email_name, context):
    body = render_to_string(template_email_name, context)
    mail.send_mail(subject, body, from_, [from_, to])