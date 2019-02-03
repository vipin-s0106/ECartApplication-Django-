from django.shortcuts import render,redirect
from .models import Mycart,MyOrder,Wishlist
from django.contrib import messages
from product.models import Accessories,Clothing,Electronics,Footwear,Product
from itertools import product

def add_to_cart(request,product_id):
    if request.user.is_authenticated:
        if Mycart.objects.filter(user=request.user,product = Product.objects.filter(id=product_id).first()).count() == 0:
            size=None
            if 'size' in request.POST:
                size = request.POST['size']
            cart = Mycart(user=request.user,product=Product.objects.filter(id=product_id).first(),size=size)
            cart.save()
            return redirect("product:product_detail",product_id)
        else:
            messages.success(request,"Already added to you cart")
            return redirect("product:product_detail",product_id)
    else:
        messages.warning(request,"Please Login")
        return redirect("user:user_login")
    
    
def move_to_cart(request,product_id):
    if request.user.is_authenticated:
        if Mycart.objects.filter(user=request.user,product = Product.objects.filter(id=product_id).first()).count() == 0:
            size=None
            if 'size' in request.POST:
                size = request.POST['size']
            cart = Mycart(user=request.user,product=Product.objects.filter(id=product_id).first(),size=size)
            cart.save()
            Wishlist.objects.filter(user=request.user,product=Product.objects.filter(id=product_id).first()).first().delete()
            return redirect("usercart:cart_view")
        else:
            messages.success(request,"Already added to you cart")
            return redirect("product:product_detail",product_id)
    else:
        messages.warning(request,"Please Login")
        return redirect("user:user_login")
    
def add_to_wishlist(request,product_id):
    if request.user.is_authenticated:
        if Wishlist.objects.filter(user=request.user,product = Product.objects.filter(id=product_id).first()).count() == 0:
            wishlist = Wishlist(user=request.user,product=Product.objects.filter(id=product_id).first())
            wishlist.save()
            return redirect("product:product_detail",product_id)
        else:
            messages.success(request,"Already added to you wishlist")
            return redirect("product:product_detail",product_id)
    else:
        messages.warning(request,"Please Login")
        return redirect("user:user_login")
    
def cart_view(request):
    products_in_cart = Mycart.objects.filter(user = request.user)
    context = {
                'products_in_cart':products_in_cart,
                'rating_range':range(5),
        }
    return render(request,'usercart/cart.html',context=context)

def wishlist_view(request):
    products_in_wishlist = Wishlist.objects.filter(user = request.user)
    context = {
                'products_in_wishlist':products_in_wishlist,
                'rating_range':range(5),
        }
    return render(request,'usercart/wishlist.html',context=context)


def remove_cart_product(request,product_id):
    Mycart.objects.filter(product = Product.objects.filter(id = product_id).first()).delete()
    return redirect('usercart:cart_view')


def remove_wishlist_product(request,product_id):
    Wishlist.objects.filter(product = Product.objects.filter(id = product_id).first()).delete()
    return redirect('usercart:wishlist_view')


def checkout(request):
    products_in_cart = Mycart.objects.filter(user = request.user)
    quantity_list = {}
    for product in products_in_cart:
        quantity_list.update({product.product.id:request.POST['quantity'+str(product.product.id)]})
    context = {
                'products_in_cart':products_in_cart,
                'quantity_list':quantity_list,
        }
    #calculating Total Amount and Store in session
    total = 0
    for product in products_in_cart:
        total += round((product.product.price - (product.product.price*product.product.offer)/100))*(int(quantity_list.get(product.product.id)))
    request.session['total_amount'] = total+60
    
    #store the Product Details to use during Payment Process and After Successfull use in MyOrder Page
    product_details = {}
    for cart_product in products_in_cart:
        product_details.update({cart_product.id:request.POST['quantity'+str(cart_product.product.id)]})  #product.id = Mycart ID using this we can access size and product details
    request.session['product_details'] = product_details
     
    #print(request.session['total_amount'],request.session['product_details']) 
    
    return render(request,'usercart/checkout.html',context=context)





    