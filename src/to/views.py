from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from das.decorators import allowed_users

# Create your views here.
@login_required(login_url="login")
def list_of_to(request):

    context = {}
    return render(request, 'list-to.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def new_to(request):
    
    context = {}

    return render(request, 'new-to.html', context)