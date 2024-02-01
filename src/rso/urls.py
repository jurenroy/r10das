from django.urls import path
from .views import *

urlpatterns = [
    path('', list_of_rso, name="list-rso"),
    path('new_so/', new_rso, name="new-rso"),
    path('edit_so/<rso_number>', edit_rso, name="edit-rso"),
    path('delete_rso/<rso_number>', delete_rso, name="delete-rso")
]