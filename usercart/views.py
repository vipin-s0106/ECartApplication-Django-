from django.shortcuts import render,redirect
from .models import Mycart,Wishlist
from django.contrib import messages
from product.models import Accessories,Clothing,Electronics,Footwear,Product
from itertools import product
from payment.models import OrderItem

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
        if cart_product.size != None:
            product_details.update({cart_product.id:str(cart_product.product.id)+":"+request.POST['quantity'+str(cart_product.product.id)]+":"+cart_product.size})  #product.id = Mycart ID using this we can access size and product details
        else:
            product_details.update({cart_product.id:str(cart_product.product.id)+":"+request.POST['quantity'+str(cart_product.product.id)]+":None"})
    request.session['product_details'] = product_details
     
    #print(request.session['total_amount'],request.session['product_details']) 
    
    return render(request,'usercart/checkout.html',context=context)


def buy_now(request,product_id):
    if request.user.is_authenticated:
        products_in_cart = Product.objects.filter(id = product_id)
        quantity_list = {}
        for product in products_in_cart:
            quantity_list.update({product.id:'1'})
        context = {
                    'products_in_cart':products_in_cart,
                    'quantity_list':quantity_list,
            }
        print(quantity_list,products_in_cart)
        #calculating Total Amount and Store in session
        total = 0
        for product in products_in_cart:
            total += round((product.price - (product.price*product.offer)/100))*(int(quantity_list.get(product.id)))
        request.session['total_amount'] = total+60
        print(request.session['total_amount'])
        #store the Product Details to use during Payment Process and After Successfull use in MyOrder Page
        product_details = {}
        for cart_product in products_in_cart:
            if 'size' in request.POST:
                product_details.update({cart_product.id:str(cart_product.id)+":1:"+request.POST['size']})  #product.id = Mycart ID using this we can access size and product details
            else:
                product_details.update({cart_product.id:str(cart_product.id)+":1:None"})
        request.session['product_details'] = product_details
           
        print(request.session['total_amount'],request.session['product_details']) 
        
        return render(request,'usercart/buy_now.html',context=context)
    else:
        messages.warning(request,"Please Login")
        return redirect("user:user_login")




def myorder(request):
    orders = OrderItem.objects.filter(user = request.user).order_by('-order_date')
    Final_Orders = []
    for order in orders:
        '''
        product_order_details sequence details 
        [[product_object,quantity,size],total_amount,address_object,transaction_type,order_date,deliver_date,status],
        '''
        product_total_orders = []
        product_order_details = []
        product_object_details = []
        for product_detal in order.product_ids_details.split(","):
            product_object_details = []
            product_object_details.append(Product.objects.filter(id = int(product_detal.split(":")[0])).first())
            product_object_details.append(product_detal.split(":")[1])
            product_object_details.append(product_detal.split(":")[2])
            product_order_details.append(product_object_details)
        product_total_orders.append(product_order_details)
        product_total_orders.append(order.total_amount)
        product_total_orders.append(order.address)
        product_total_orders.append(order.transaction_type)
        product_total_orders.append(order.order_date)
        product_total_orders.append(order.deliver_date)
        product_total_orders.append(order.status)
        product_total_orders.append(order.id)
        Final_Orders.append(product_total_orders)
    context = {
        'Final_Orders':Final_Orders
        }
    return render(request,"usercart/myorder.html",context=context)


def cancel_order(request,order_id):
    order = OrderItem.objects.filter(id = order_id).first()
    order.status = "Cancelled"
    order.save()
    return redirect('usercart:myorder')



    