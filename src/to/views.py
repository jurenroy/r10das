from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def list_of_to(request):
    
    context = {}
    return render(request, 'list-to.html', context)