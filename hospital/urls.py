from django.urls import path
#from .views import About, Home, Contact, Login
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('admin_login/', views.Login, name='login'),
    path('logout/', views.LogoutAdmin, name='logout'),
    path('dashboard/', views.Index, name='dashboard',),
    path('view-doctor/', views.ViewDoctor, name='view-doctor'),
    path('delete-doctor/<str:pk>/', views.DeleteDoctor, name="delete-doctor"),
    path('add-doctor/', views.AddDoctor, name='add-doctor'),
    path('view-patient/', views.ViewPatient, name='view-patient'),
    path('delete-patient/<str:pk>/', views.DeletePatient, name="delete-patient"),
    path('add-patient/', views.AddPatient, name='add-patient'),
    path('view-appointment/', views.ViewAppointment, name='view-appointment'),
    path('delete-appointment/<str:pk>/', views.DeleteAppointment, name="delete-appointment"),
    path('add-appointment/', views.AddAppointment, name='add-appointment'),

]