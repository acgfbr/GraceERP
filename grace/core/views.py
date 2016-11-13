from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from grace.core.forms import HomeContactForm

# Create your views here.
def home(request):

    if request.method == 'POST':

        form = HomeContactForm(request.POST)

        if form.is_valid():
            form.full_clean()
            body = render_to_string('contact_email.txt',
                                    form.cleaned_data)
            mail.send_mail('Requisição de contato Grace ERP',
                           body,
                           form.cleaned_data['ur_email'],
                           ['sir.vavo@gmail.com'])

            return HttpResponseRedirect('/')

        else:
            return render(request, 'index.html', {'form': form})
    else:
        context = {'form': HomeContactForm()}
        return render(request, 'index.html', context)
