from django.shortcuts import render,redirect
from django.contrib import messages
from unicodedata import category
from django.db.models import Q
from usercart.models import Mycart
from user.models import Address
from .models import OrderItem

# Create your views here.

def create_order(request):
    address_list = Address.objects.filter(user = request.user)
    if request.method == "POST":
        address_id = request.POST['address']
        payment_mode = request.POST['paymentmode']
        if payment_mode == "paypal" or payment_mode == "cod":
            total_amount = request.session['total_amount']
            product_details = request.session['product_details']
            product_details_string = []
            for key,value in product_details.items():
                product_details_string.append(value.split(":")[0]+":"+value.split(":")[1]+":"+value.split(":")[2])
            product_details_string = ",".join(product_details_string)
            address = Address.objects.filter(id=address_id).first()
            orderitem = OrderItem(product_ids_details=product_details_string,total_amount=total_amount,address=address,user=request.user)
            if payment_mode == "paypal":
                pass
            elif payment_mode == "cod":
                orderitem.status = "Order Placed"
                orderitem.save()
                for product in Mycart.objects.all():
                    product.delete()
                messages.success(request,"Your order has been placed successfully!")
                return redirect('usercart:myorder')
            else:
                pass
        else:
            messages.warning(request, "Payment mode - "+payment_mode+" Under Development! Please use Paypal or COD mode")
            return redirect('payment:create_order')
    context = {
        'address_list':address_list
        }
    return render(request,'payment/create_order.html',context=context)