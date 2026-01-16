from django.urls import path
from cash import views

urlpatterns = [
    path('', views.cash, name='cash') 
   ]