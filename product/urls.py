from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'product'

urlpatterns = [
   url('^$',views.home,name="home"),
   url('^mens_product/$',views.mens_product,name="mens_product"),
   url('^detail/(?P<product_id>[0-9]+)/$',views.product_detail,name="product_detail"),
]