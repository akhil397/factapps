from django.urls import path
from factapp import views

urlpatterns = [
    path('', views.home, name='home') 
   ]