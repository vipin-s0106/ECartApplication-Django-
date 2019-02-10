from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'product'

urlpatterns = [
   url('^$',views.home,name="home"),
   url('^mens_product/$',views.mens_product,name="mens_product"),
   url('^womens_product/$',views.womens_product,name="womens_product"),
   url('^mens_shoes/$',views.mens_shoes_product,name="mens_shoes_product"),
   url('^womens_shoes/$',views.womens_shoes_product,name="womens_shoes_product"),
   url('^mens_accessories/(?P<wear_category>[a-zA-Z0-9@#$&-]+)/$',views.mens_accessories_product,name="mens_accessories_product"),
   url('^womens_accessories/(?P<wear_category>[a-zA-Z0-9@#$&-]+)/$',views.womens_accessories_product,name="womens_accessories_product"),
   url('^mens_wear_product/(?P<wear_category>[a-zA-Z0-9@#$&-]+)/$',views.mens_wear_product,name="mens_wear_product"),
   url('^womens_wear_product/(?P<wear_category>[a-zA-Z0-9@#$&-]+)/$',views.womens_wear_product,name="womens_wear_product"),
   url('^electronics_product/(?P<sub_category>[a-zA-Z0-9@#$&-]+)/$',views.electronics_product,name="electronics_product"),
   url('^tv_appliance_product/(?P<sub_category>[a-zA-Z0-9@#$&-]+)/$',views.tv_appliance_product,name="tv_appliance_product"),
   url('^detail/(?P<product_id>[0-9]+)/$',views.product_detail,name="product_detail"),
   url('^comment/(?P<product_id>[0-9]+)/$',views.write_reviews,name="write_reviews"),
   url('^search_product/$',views.search_product,name="search_product"),
]
