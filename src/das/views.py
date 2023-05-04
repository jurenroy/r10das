from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import sweetify

from .decorators import unauthenticated_user

@unauthenticated_user
def signin(request):
    context = {}

    if request.POST:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            sweetify.error(request, 'Incorrect username/password', persistent='Close')
            context = {
                'username': request.POST.get('username')
            }

    return render(request, 'login.html', context)