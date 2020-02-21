from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .decorator import unautehticated_user,allowed_users,admin_only


@login_required(login_url='login')
@admin_only
def home(request):
    return render(request,'accounts/login.html')

def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['email'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{"error":"email or password is incorrect!"})
    else:
        return render(request,'accounts/login.html')


def admin(request):
    return render(request,'accounts/homepage.html',{'user_admin':'admin'})


def manager(request):
    return render(request,'accounts/homepage.html',{'user_manager':'manager'})

def employee(request):
    return render(request,'accounts/homepage.html',{'user_employee':'employee'})


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('home')

def apply_leave(request):
    return render(request,'accounts/apply_leave.html')
