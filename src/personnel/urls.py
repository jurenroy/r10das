from django.urls import path
from .views import *


urlpatterns = [
    path('', list_of_personnel, name="list-of-personnel"),
    path('new-employee/', add_employee, name="add-employee"),
    path('bulk-upload/', bulk_upload, name="bulk-upload")
]