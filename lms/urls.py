from django.urls import path,include
from accounts import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('account/',include('accounts.urls'))
]
