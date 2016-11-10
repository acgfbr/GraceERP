from django.shortcuts import render
from grace.members_area.forms import MemberAreaForm

def members(request):
    context = {'form': MemberAreaForm()}
    return render(request, 'members_area/members_area_form.html', context)