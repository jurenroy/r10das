from django import template
from django.contrib.auth.models import User
from rso.models import rso_assinged_personnel

register = template.Library()

# Hide columns when user group is "users"
@register.filter(name="user_group")
def user_group(user):
    user = User.objects.get(id = user.id)
    return user.groups.all()[0].name

# Check if the remarks is empty
@register.filter(name="empty")
def empty(value):
    if value == None or value == "":
        return "-"
    else:
        return value
    
# Get assigned personnel
@register.filter(name="get_assigned_personnel")
def get_assigned_personnel(rso):
    assigned = []
    personnels = rso_assinged_personnel.objects.filter(rso = rso)

    for personnel in personnels:
        if personnel.employee.personnel.personnel_mi is None:
            assigned.append(f"{ personnel.employee.first_name } { personnel.employee.last_name }")
        else:
            assigned.append(f"{ personnel.employee.first_name } { personnel.employee.personnel.personnel_mi } { personnel.employee.last_name }")

    assigned = ", ".join(assigned)

    return assigned