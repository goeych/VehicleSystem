from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,Group




# Create your models here.

class User(AbstractUser):
    email           = models.EmailField(blank = True,unique=True)
    username        = models.CharField(max_length=255,blank=True,null=True)
    name            = models.CharField(max_length=200,blank=True,null=True)
    first_name      = models.CharField(max_length=255,blank=True,null=True)
    last_name       = models.CharField(max_length=255,blank=True,null=True)


    USERNAME_FIELD  = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(Group)  # Add this line to associate groups with users

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name or self.email.split('@')[0] if self.name else ''
    

    


