from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from rso.models import rso_assinged_personnel
from das.decorators import allowed_users
import os
from django.http import JsonResponse


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

@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def edit_rso(request, rso_number):
    rso_details = get_object_or_404(RSO, rso_number = rso_number)
    rso_edit_form = RSOEditForm(instance=rso_details)
    assigned_personnels = rso_assinged_personnel.objects.filter(rso_id = rso_number)
    personnels = User.objects.filter(is_superuser = False).order_by('last_name')

    if request.method == "POST":
        rso_form = RSOForm(request.POST, request.FILES, instance=rso_details)
        if rso_form.is_valid():
            rso_form_save = rso_form.save()
            for emp in request.POST.getlist('personnel_assigned'):
                employee_exist = rso_assinged_personnel.objects.filter(employee_id = emp, rso_id = rso_number).first()
                if not employee_exist:
                    employee = User.objects.get(id = emp)
                    rso_assinged_personnel.objects.create(rso = rso_form_save, employee = employee)

    context = {
        'rso_edit_form': rso_edit_form,
        'rso_assigned_personnel': rso_details,
        'assigned_personnels': assigned_personnels,
        'personnels': personnels,
        'rso_number': rso_number
    }

    return render(request, 'edit-rso.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def delete_rso(request, rso_number):
    if request.method == "POST":
        rso_assinged_personnel.objects.filter(rso_id = rso_number).delete()
        rso = RSO.objects.get(rso_number=rso_number)

        file_path = str(rso.rso_scan_copy.path)

        if os.path.exists(file_path):
            rso.delete()
            os.remove(file_path)
        else:
            print(False)

        return JsonResponse({'message': 'Delete success'}, safe=False)
