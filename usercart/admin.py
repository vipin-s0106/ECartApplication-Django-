from django.contrib import admin

# Register your models here.
from .models import Mycart,Wishlist

admin.site.register(Mycart)
admin.site.register(Wishlist)
