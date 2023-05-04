from django.http import HttpResponse
from django.shortcuts import redirect

# Restrict logged_in user to access login page
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('dashboard')

        return view_func(request, *args, **kwargs)
    return wrapper_func

# Restrict users to access pages they are not allowed
def allowed_users(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You not authorized to view this page')

            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator