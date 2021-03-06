from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('ProductsApp:home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func





def allowed_users(allowed_role=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            print('working',allowed_role)
            group=None
            if request.user.groups.exists():
                group= request.user.groups.all()[0].name

            if group in allowed_role:
                return view_func(request, *args, **kwargs)
            else:
                return redirect("/user/")
        return wrapper_func
    return decorator





def logout_req(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse('siz bu saytdan avtorizatsiya qilgansiz')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func





def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group=='customer':
            return redirect('user')
        if group=='admin':
            return  view_func(request, *args, **kwargs)
    return wrapper_function