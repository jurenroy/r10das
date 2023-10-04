from django.shortcuts import render

# Create your views here.
def list_of_personnel(request):
    
    context = {}

    return render(request, 'list-of-employee.html', context)