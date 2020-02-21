from django.http import HttpResponse
from django.shortcuts import redirect

def unautehticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):

            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                print(group)
                return HttpResponse('You are not authorised to acess this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group=='admin':
            return redirect('admin')
        if group=='manager':
            return redirect('manager')
        if group=='employee':
            return redirect('employee')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func
