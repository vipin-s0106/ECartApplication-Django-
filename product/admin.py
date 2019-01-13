from django.contrib import admin
from .models import Product,ProductInfo,Clothing,Footwear,Accessories,Electronics
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductInfo)
admin.site.register(Clothing)
admin.site.register(Footwear)
admin.site.register(Electronics)
admin.site.register(Accessories)

