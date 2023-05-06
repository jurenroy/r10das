from django.shortcuts import render, redirect
from .forms import *
from rso.models import rso_assinged_personnel
# from das.decorators 

# Create your views here.
def list_of_rso(request):
    rsos = RSO.objects.all()

    context = {
        'rsos': rsos
    }

    return render(request, 'list-rso.html', context)

def new_rso(request):
    rso_form = RSOForm()
    personnels = User.objects.filter(is_superuser = False).order_by('last_name')

    if request.method == "POST":
        rso_form = RSOForm(request.POST, request.FILES)
        if rso_form.is_valid():
            rso_form_save = rso_form.save()
            for emp in request.POST.getlist('personnel_assigned'):
                employee = User.objects.get(id = emp)
                rso_assinged_personnel.objects.create(rso = rso_form_save, employee = employee)

            return redirect('dashboard')

    context = {
        'rso_form': rso_form,
        'personnels': personnels
    }

    return render(request, 'new-rso.html', context)