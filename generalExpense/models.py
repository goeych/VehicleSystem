from django.db import models
#from django.contrib.auth.models import User
from accounts.models import User



# Create your models here.

class Customer(models.Model):
    user            = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    name            = models.CharField(max_length = 200,null=True,blank=True)
    phone           = models.CharField(max_length = 200, null=True,blank=True)
    email           = models.CharField(max_length = 200, null=True,blank=True)
    date_updated    = models.DateTimeField(auto_now = True,null=True)
    date_created    = models.DateTimeField(auto_now_add = True,null=True,blank=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    customer        = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE)
    name            = models.CharField(max_length = 200,null=True)
    platenumber     = models.CharField(max_length = 200,null=True)
    yearpurchase    = models.DateField(null=True,blank=True)
    colour          = models.CharField(max_length = 200, null = True)
    capacity        = models.CharField(max_length = 200, null = True)
    profile_pic     = models.ImageField(default="profile.jpg",null=True,blank=True)
    date_created    = models.DateTimeField(auto_now_add = True,null=True)
    date_updated    = models.DateTimeField(auto_now = True,null=True)

    def __str__(self):
        return self.platenumber

class Vehicleexpense(models.Model):

    CATEGORY = (
        ('Regular','Regular'),
        ('Emergency','Emergency'),
        ('Plan','Plan'),
        )
    
    vehicle         = models.ForeignKey(Vehicle, null=True,on_delete = models.SET_NULL)
    customer        = models.ForeignKey(Customer,null=True,blank=True,on_delete = models.SET_NULL)
    name            = models.CharField(max_length = 200,null=True,blank=True)
    price           = models.FloatField(null=True,blank=True)
    category        = models.CharField(max_length = 200,null=True,blank=True,choices = CATEGORY)
    mileage         = models.FloatField(null=True,blank=True)
    description     = models.CharField(max_length = 200,null=True,blank=True)
    date_created    = models.DateTimeField(null=True,blank=True)
    date_updated    = models.DateTimeField(auto_now=True,null=True)
    note            = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date_created']  # Sort by date_created field in descending order

class Dailyexpense(models.Model):

    CATEGORY = (
        ('Regular','Regular'),
        ('Emergency','Emergency'),
        ('Plan','Plan'),
        )

    customer        = models.ForeignKey(Customer,null=True,blank=True,on_delete = models.SET_NULL)
    name            = models.CharField(max_length = 200,null=True,blank=True)
    price           = models.FloatField(null=True,blank=True)
    category        = models.CharField(max_length = 200,null=True,blank=True,choices = CATEGORY)
    description     = models.CharField(max_length = 200,null=True,blank=True)
    date_created    = models.DateTimeField(null=True,blank=True)
    date_updated    = models.DateTimeField(auto_now=True,null=True)
    note            = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date_created']  # Sort by date_created field in descending order
        
