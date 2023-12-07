from django.urls import path
from .views import *


urlpatterns = [
    path('', list_of_personnel, name="list-of-personnel"),
    path('new-employee/', add_employee, name="add-employee"),
    path('change-password/', change_password, name="change-password"),
    path('201-files/', personal_files, name="201-files")
]