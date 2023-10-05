from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def list_of_personnel(request):
    
    context = {}

    return render(request, 'list-of-employee.html', context)

def add_employee(request):

    personnel_form = PersonnelForm()

    if request.method == "POST":
        personnel_form = PersonnelForm(request.POST)
        if personnel_form.is_valid():
            # Clean data
            pass

    context = {
        'personnel_form': personnel_form
    }
    return render(request, 'new-employee.html', context)