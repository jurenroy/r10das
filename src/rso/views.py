from django.shortcuts import render
from .forms import *

# Create your views here.
def list_of_rso(request):
    context = {}

    return render(request, 'list-rso.html', context)

def new_rso(request):
    rso_form = RSOForm()
    personnels = Personnel.objects.select_related('user')

    context = {
        'rso_form': rso_form,
        'personnels': personnels
    }

    return render(request, 'new-rso.html', context)