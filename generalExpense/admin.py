from django.contrib import admin

from .models import Vehicle,Vehicleexpense,Customer,Dailyexpense

# Register your models here.

admin.site.register(Vehicle)
admin.site.register(Vehicleexpense)
admin.site.register(Customer)
admin.site.register(Dailyexpense)

