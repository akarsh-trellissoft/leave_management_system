from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('apply_leave/',views.apply_leave,name='apply_leave'),
    path('login/',views.login,name='login'),
    path('employee/',views.employee,name='employee'),
    path('manager/',views.manager,name='manager'),
    path('admin/',views.admin,name='admin'),
    path('logout/',views.logout,name="logout")
]
