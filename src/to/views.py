from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from das.decorators import allowed_users
from personnel.models import Personnel
from .forms import *

# Create your views here.
@login_required(login_url="login")
def list_of_to(request):
    group = request.user.groups.all()[0].name

    if group == "users":
        tos = TO.objects.filter(to_assigned_personnel__employee = request.user)
    else:
        tos = TO.objects.all()

    context = {
        'tos': tos
    }

    return render(request, 'list-to.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def new_to(request):
    
    to_form = TOForm()

    if request.method == "POST":
        to_form = TOForm(request.POST, request.FILES)
        if to_form.is_valid():
            to_form_save = to_form.save()
            employee = User.objects.get(id = request.POST.get('personnel'))
            to_assigned_personnel.objects.create(to = to_form_save, employee = employee)

        return redirect('list-to')

    context = {
        'to_form': to_form
    }

    return render(request, 'new-to.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def personnel_data(request):

    # Get the ID from the request
    id = request.GET.get('id')

    try:
        personnel_object = Personnel.objects.get(user = id)
        personnel_data = {
            'personnel_id_number'   : personnel_object.personnel_id_number,
            'personnel_mi'          : personnel_object.personnel_mi,
            'personnel_division'    : {
                'division': personnel_object.personnel_division.division_name,
                'division_shorthand_name': personnel_object.personnel_division.division_shorthand_name
            },
            'personnel_position'    : personnel_object.personnel_position,
            'personnel_station'     : personnel_object.personnel_station,
        }
        return JsonResponse(personnel_data)
    except Personnel.DoesNotExist:
        return JsonResponse({'error': 'Personnel not found'}, status=404)