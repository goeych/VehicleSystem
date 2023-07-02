from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #add this model for Group
from .models import User

# Register your models here.

admin.site.register(User,UserAdmin) #add this UserAdmin model for Group

class CustomUserAdmin(UserAdmin):  #add this model for Group
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('groups',)}),
    )

