from django import template
from usercart.models import Mycart,Wishlist
from product.models import Product,Accessories,Clothing,Electronics,Footwear,ProductInfo
from payment.models import OrderItem
from datetime import datetime,timedelta

register = template.Library()

@register.filter(name = 'get_discounted_price')
def get_discounted_price(price,offer):
    discounted_price = round((price - (price*offer)/100))
    return discounted_price
    
    
@register.filter(name = 'get_user_cart_value')
def get_user_cart_value(user):
    cart_count = Mycart.objects.filter(user = user).count()
    return cart_count


@register.filter(name= 'get_user_wishlist_value')
def get_user_wishlist_value(user):
    wishlist_count = Wishlist.objects.filter(user = user).count()
    return wishlist_count

@register.filter(name = 'get_cart_total')
def get_cart_total(user):
    products = Mycart.objects.filter(user = user)
    total = 0
    for cart_product in products:
        if cart_product.product.offer > 0:
            total +=  round(cart_product.product.price - (cart_product.product.price*cart_product.product.offer)/100)
        else:
            total += cart_product.product.price
        
    return total


@register.filter(name= 'split_text')
def split_text(size):
    return size.split(',')

 
@register.filter(name= 'description_split')   
def description_split(product_id):
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
    description = product.description.split(";")
    if len(description) > 4:
        for i in range (4,len(description)):
            description.pop()
    return description

@register.filter(name= 'get_product_total_reviews')
def get_product_total_reviews(product_id):
    return ProductInfo.objects.filter(product = Product.objects.filter(id = product_id).first())
    
@register.filter(name= 'size_split_text')   
def size_split_text(product_id):
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
    if product.size == None:
        return None
    else:
        return product.size.split(',')
    
    
@register.filter(name="average_rating")
def average_rating(product_id):
    product_info = ProductInfo.objects.filter(product = Product.objects.filter(id = product_id).first())
    sum = 0
    for product in product_info:
        sum += product.rating
    if product_info.count() == 0:
        return 0
    else:
        return round(sum/product_info.count())


@register.filter(name = "get_quantity_total")
def get_quantity_total(product_id,quantity):
    product = Product.objects.filter(id = product_id).first()
    discounted_price = round((product.price - (product.price*product.offer)/100))
    return discounted_price*(int(quantity))

@register.filter(name = "get_sub_total")
def get_sub_total(products,quantity_list):
    sub_total = 0
    for product in products:
        sub_total += round((product.product.price - (product.product.price*product.product.offer)/100))*(int(quantity_list.get(product.product.id)))
    return sub_total

@register.filter(name = "get_total")
def get_total(products,quantity_list):
    total = 0
    for product in products:
        total += round((product.product.price - (product.product.price*product.product.offer)/100))*(int(quantity_list.get(product.product.id)))
    return total+60

@register.filter(name = "get_order_status")    
def get_order_status(order_id):
    order = OrderItem.objects.filter(id = int(order_id)).first()
    if datetime.now().strftime('%Y-%m-%d') < (datetime.strptime(order.deliver_date, '%Y-%m-%d') + timedelta(days=3)).strftime('%Y-%m-%d'):
        order.status = "In Shipping"
        order.save()      
    elif datetime.now().strftime('%Y-%m-%d') >= order.deliver_date:
        order.status = "Delivered"
        order.save()  
    return order.status
    