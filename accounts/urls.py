from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register , name='register'),
    path('login/', views.loginUser , name='loginUser'),
    path('logout/', views.logoutUser , name='logoutUser'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('', views.dashboard , name='dashboard'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

] 
