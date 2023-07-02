from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('addVehicleexpense/<str:pk>/',views.addVehicleexpense,name='addVehicleexpense'),
    path('updateVehicleexpense/<str:pk>/',views.updateVehicleexpense,name='updateVehicleexpense'),
    path('deleteVehicleexpense/<str:pk>/',views.deleteVehicleexpense,name='deleteVehicleexpense'),

    path('addDailyexpense/<str:pk>/',views.addDailyexpense,name='addDailyexpense'),
    path('updateDailyexpense/<str:pk>/',views.updateDailyexpense,name='updateDailyexpense'),
    path('deleteDailyexpense/<str:pk>/',views.deleteDailyexpense,name='deleteDailyexpense'),



    ]
