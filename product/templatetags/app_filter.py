from django import template
from usercart.models import Mycart,Wishlist


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
    wishlist_count = Wishlist.objects.filter(user = user)
    return wishlist_count