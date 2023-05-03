from django.shortcuts import render


# Create your views here.
def list_of_rso(request):
    context = {}

    return render(request, 'list-rso.html', context)