from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import *
from .forms import *

# Create your views here.
def list_of_personnel(request):

    # Retrieve list of personnel sorted by id number
    personnels = Personnel.objects.select_related('user')

    context = {
        'personnels': personnels
    }

    return render(request, 'list-of-employee.html', context)

def add_employee(request):

    personnel_form = PersonnelForm()

    if request.method == "POST":
        personnel_form = PersonnelForm(request.POST)
        if personnel_form.is_valid():

            # Clean data
            id_number   = personnel_form.cleaned_data['id_number']
            first_name  = personnel_form.cleaned_data['first_name']
            middlename  = personnel_form.cleaned_data['middlename']
            last_name   = personnel_form.cleaned_data['last_name']
            suffix      = personnel_form.cleaned_data['suffix']
            username    = personnel_form.cleaned_data['username']
            password    = make_password(personnel_form.cleaned_data['password'])
            user_type   = personnel_form.cleaned_data['groups']
            division    = personnel_form.cleaned_data['division']
            section     = personnel_form.cleaned_data['section']
            position    = personnel_form.cleaned_data['position']
            designation = personnel_form.cleaned_data['designation']
            station     = personnel_form.cleaned_data['official_station']
            signatory   = personnel_form.cleaned_data['signatory']
            date_joined = personnel_form.cleaned_data['date_joined']

            # Make an instance of user
            personnel_form_instance = User(
                is_superuser=False,
                password=password,
                username=username,
                first_name=first_name,
                last_name=last_name,
                date_joined=date_joined
            )

            # Save personnel information to user table
            personnel_form_instance_save = personnel_form_instance.save()

            # Retrieve the selected group and add the user to the selected group
            groups = Group.objects.filter(name=user_type)
            personnel_form_instance.groups.set(groups)

            # Add misc details to the personnel table
            Personnel.objects.create(
                user = personnel_form_instance,
                personnel_id_number = id_number,
                personnel_mi = middlename,
                personnel_division = division,
                personnel_section = section,
                personnel_position = position,
                personnel_station = station,
                personnel_suffix = suffix,
                signatory = signatory
            )

            return redirect('list-of-personnel')

    context = {
        'personnel_form': personnel_form
    }
    return render(request, 'new-employee.html', context)

# For bulk upload
def bulk_upload(request):

    context = {}
    return render(request, 'bulk_upload.html',context)