from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Address,Payment

#make Framework to use Custom user Model For to store Admin Detail to Databases
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('name','username','password','email','mobile','birthdate','is_active','is_staff','date_joined'),
        }),
    )
    model = User
    list_display = ['username','password','email','is_staff']
    
    
admin.site.register(User,CustomUserAdmin)
admin.site.register(Address)
admin.site.register(Payment)


