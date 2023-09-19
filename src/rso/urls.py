from django.urls import path
from .views import *

urlpatterns = [
    path('', list_of_rso, name="list-rso"),
    path('new_so/', new_rso, name="new-rso"),
]