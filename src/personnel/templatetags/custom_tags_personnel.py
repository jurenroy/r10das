from django import template
from django.contrib.auth.models import User
from personnel.models import *

register = template.Library()

@register.filter(name="fullname")
def fullname(personnel):

    personnel_data = Personnel.objects.select_related('user').get(user = personnel.user)

    if personnel_data.personnel_mi == None:
        if personnel_data.personnel_suffix == None:
            fullname = f"{ personnel_data.user.last_name }, { personnel_data.user.first_name }"
        else:
            fullname = f"{ personnel_data.user.last_name }, { personnel_data.user.first_name } { personnel_data.personnel_suffix }"
    else:
        if personnel_data.personnel_suffix == None:
            fullname = f"{ personnel_data.user.last_name }, { personnel_data.user.first_name } { personnel_data.personnel_mi[0] }."
        else:
            fullname = f"{ personnel_data.user.last_name }, { personnel_data.user.first_name } { personnel_data.personnel_mi[0] }. { personnel_data.personnel_suffix }"

    return fullname

@register.filter(name="designation")
def designation(designation):

    if designation == "RD":
        designation = "Regional Director"
    elif designation == "DC":
        designation = "Division Chief"
    elif designation == "SC":
        designation = "Section Chief"
    else:
        designation = "-"

    return designation