from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.my_form,name='register'),
    path('login/', views.login,name='login'),
    path('planSelection/', views.planSelection,name='planSelection'),
    path('MainPage/', views.dashboard,name='MainPage'),

]