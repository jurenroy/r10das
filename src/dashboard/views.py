from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    context = {}

    return render(request, 'dashboard.html', context)

def signout(request):
    logout(request)
    return redirect('login')