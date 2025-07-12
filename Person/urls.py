from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/' , login_user , name="login_user"),
    
    path('logout/',LogoutView.as_view(), name="logout")
   


]
