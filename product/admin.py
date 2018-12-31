from django.contrib import admin
from .models import Product,Mycart,ProductInfo,Wishlist,Clothing,Footwear,Accessories,Electronics,MyOrder
# Register your models here.

admin.site.register(Product)
admin.site.register(Mycart)
admin.site.register(ProductInfo)
admin.site.register(Wishlist)
admin.site.register(Clothing)
admin.site.register(Footwear)
admin.site.register(Electronics)
admin.site.register(Accessories)
admin.site.register(MyOrder)
