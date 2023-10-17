from django import template
from datetime import datetime
from django.contrib.auth.models import User
from to.models import to_assigned_personnel

register = template.Library()

@register.filter(name="user_group")
def user_group(user):
    user = User.objects.get(id = user.id)
    return user.groups.all()[0].name

@register.filter(name="get_personnel_info")
def get_personnel_info(to, option):
    assigned_personnel = to_assigned_personnel.objects.get(to = to)

    if option == "name":
        if assigned_personnel.employee.personnel.personnel_mi:
            name = f"{ assigned_personnel.employee.last_name }, { assigned_personnel.employee.first_name } { assigned_personnel.employee.personnel.personnel_mi }"
        else:
            name = f"{ assigned_personnel.employee.last_name }, { assigned_personnel.employee.first_name }"

        return name
    elif option == "position":
        return assigned_personnel.employee.personnel.personnel_position
    elif option == "division":
        return assigned_personnel.employee.personnel.personnel_division
    elif option == "station":
        return assigned_personnel.employee.personnel.personnel_station

@register.filter(name="travel_date")
def travel_data(to):
    # Assuming 'to.to_departure' is a string in the format "YYYY-MM-DD"
    departure_date_str = str(to.to_departure)
    departure = datetime.strptime(departure_date_str, "%Y-%m-%d")

    arrival_date_str = str(to.to_arrival)
    arrival = datetime.strptime(arrival_date_str, "%Y-%m-%d")

    # Format 'departure' as "mm-dd-YYYY"
    formatted_departure = departure.strftime("%m/%d/%Y")
    formatted_arrival = arrival.strftime("%m/%d/%Y")

    # Combine the formatted departure date with 'to.to_arrival'
    result = f"{ formatted_departure } - { formatted_arrival }"

    # Return the result
    return result