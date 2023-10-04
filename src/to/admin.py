from django.contrib import admin
from .models import *

# Register your models here.
class TOAdmin(admin.ModelAdmin):
    list_display = ['to_number', 'to_date', 'to_departure', 'to_arrival', 'to_destination']

class AssignedPersonnelAdmin(admin.ModelAdmin):
    list_display = ['get_to', 'get_employee']

    @admin.display(description="TO Number and Subject")
    def get_to(self, object):
        return f"{ object.to.to_number }"
    
    @admin.display(description="Personnel")
    def get_employee(self, object):
        return f"{ object.employee.last_name }, { object.employee.first_name } { object.employee.personnel.personnel_mi }"

admin.site.register(TO, TOAdmin)
admin.site.register(to_assigned_personnel, AssignedPersonnelAdmin)