from django.shortcuts import render
from grace.core.forms import HomeContactForm

# Create your views here.

def home(request):
    context = {'form': HomeContactForm()}
    return render(request, 'index.html', context)