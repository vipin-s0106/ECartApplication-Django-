from django.contrib import admin

# Register your models here.
from .models import Mycart,MyOrder,Wishlist,Payment

admin.site.register(Mycart)
admin.site.register(MyOrder)
admin.site.register(Wishlist)
admin.site.register(Payment)