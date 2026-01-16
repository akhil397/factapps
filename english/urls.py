from django.urls import path
from data import views

urlpatterns = [
    path('', views.english, name='english') 
   ]