from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from rso.models import rso_assinged_personnel
from das.decorators import allowed_users

# Create your views here.
@login_required(login_url="login")
def list_of_rso(request):
    group = request.user.groups.all()[0].name

    if group == "users":
        rsos = RSO.objects.filter(rso_assinged_personnel__employee = request.user)
    else:
        rsos = RSO.objects.all()

    context = {
        'rsos': rsos
    }

    return render(request, 'list-rso.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
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

            return redirect('list-rso')

    context = {
        'rso_form': rso_form,
        'personnels': personnels
    }

    return render(request, 'new-rso.html', context)