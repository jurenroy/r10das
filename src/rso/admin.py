from django.contrib import admin
from .models import *

# Register your models here.
class RSOAdmin(admin.ModelAdmin):
    list_display = ['rso_number', 'rso_subject', 'rso_date', 'rso_scheduled_dates_from', 'rso_scheduled_dates_to']

class AssignedPersonnelAdmin(admin.ModelAdmin):
    list_display = ['get_rso', 'get_employee']

    @admin.display(description="RSO Number and Subject")
    def get_rso(self, object):
        return f"{ object.rso.rso_number } - { object.rso.rso_subject }"
    
    @admin.display(description="Personnel")
    def get_employee(self, object):
        return f"{ object.employee.last_name }, { object.employee.first_name } { object.employee.personnel.personnel_mi }"

admin.site.register(RSO, RSOAdmin)
admin.site.register(rso_assinged_personnel, AssignedPersonnelAdmin)