from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),

    path('accountSettings/',views.accountSettings,name='accountSettings'),
    
]
