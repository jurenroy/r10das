from django.urls import path
from .views import *

urlpatterns = [
    path('', list_of_to, name="list-to"),
]