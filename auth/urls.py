from django.urls import path
from auth import views

urlpatterns = [
    path('', views.login, name='login') 
   ]