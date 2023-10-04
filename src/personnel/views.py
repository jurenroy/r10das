from django.shortcuts import render

# Create your views here.
def list_of_personnel(request):
    
    context = {}

    return render(request, 'list-of-employee.html', context)

def add_employee(request):

    context = {}
    return render(request, 'new-employee.html', context)