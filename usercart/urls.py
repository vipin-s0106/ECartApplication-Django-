from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'usercart'

urlpatterns = [
   url('^add_to_cart/(?P<product_id>[0-9]+)/$',views.add_to_cart,name="add_to_cart"),
   url('^move_to_cart/(?P<product_id>[0-9]+)/$',views.move_to_cart,name="move_to_cart"),
   url('^add_to_wishlist/(?P<product_id>[0-9]+)/$',views.add_to_wishlist,name="add_to_wishlist"),
   url('^cart/$',views.cart_view,name="cart_view"),
   url('^wishlist/$',views.wishlist_view,name="wishlist_view"),
   url('^removecartproduct/(?P<product_id>[0-9]+)/$',views.remove_cart_product,name="remove_cart_product"),
   url('^removewishlistproduct/(?P<product_id>[0-9]+)/$',views.remove_wishlist_product,name="remove_wishlist_product"),
   url('^checkout/$',views.checkout,name="checkout"),
   url('^buy_now/(?P<product_id>[0-9]+)/$',views.buy_now,name="buy_now"),
   url('^myorder/$',views.myorder,name="myorder"),
   url('^view_order_graph/$',views.view_order_graph,name="view_order_graph"),
   url('^cancel_order/(?P<order_id>[0-9]+)/$',views.cancel_order,name="cancel_order"),
]
