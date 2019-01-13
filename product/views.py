from django.shortcuts import render
from .models import Product,ProductInfo,Clothing,Accessories,Electronics,Footwear



def home(request):
    return render(request,'product/home.html')



def mens_product(request):
    products = Clothing.objects.filter(gender = "M")
    context = {'products':products
                }
    return render(request,'product/mens_product.html',context=context)


def product_detail(request,product_id):
    if Clothing.objects.filter(product = Product.objects.filter(id = product_id).first()).first() is not None:
        product = Clothing.objects.filter(product = Product.objects.filter(id = product_id).first()).first()
    elif Footwear.objects.filter(product = Product.objects.filter(id = product_id).first()).first() is not None:
        product = Footwear.objects.filter(product = Product.objects.filter(id = product_id).first()).first()
    elif Accessories.objects.filter(product = Product.objects.filter(id = product_id).first()).first() is not None:
        product = Accessories.objects.filter(product = Product.objects.filter(id = product_id).first()).first()
    elif Electronics.objects.filter(product = Product.objects.filter(id = product_id).first()).first() is not None:
        product = Electronics.objects.filter(product = Product.objects.filter(id = product_id).first()).first()
    else:
        pass
                        
    product_reviews = ProductInfo.objects.filter(product = product.product)
    
    context = { 'product':product,
                'product_reviews':product_reviews
        }
    
    return render(request,'product/product_detail.html',context=context)

