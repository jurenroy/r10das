from django.urls import path
from .views import *

urlpatterns = [
    path('', list_of_to, name="list-to"),
    path('new_to/', new_to, name="new-to"),
]