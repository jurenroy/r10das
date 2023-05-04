from django.shortcuts import render
from .forms import *
from rso.models import rso_assinged_personnel
# from das.decorators 

# Create your views here.
def list_of_rso(request):
    context = {}

    return render(request, 'list-rso-admin.html', context)

def new_rso(request):
    rso_form = RSOForm()
    personnels = User.objects.filter(is_superuser = False).order_by('last_name')

    if request.method == "POST":
        rso_form = RSOForm(request.POST, request.FILES)
        if rso_form.is_valid():
            rso_form_save = rso_form.save()
            for emp in request.POST.getlist('personnel_assigned'):
                employee = User.objects.get(id = emp)
                print(employee)
                rso_assinged_personnel.objects.create(rso = rso_form_save, employee = employee)

    context = {
        'rso_form': rso_form,
        'personnels': personnels
    }

    return render(request, 'new-rso.html', context)