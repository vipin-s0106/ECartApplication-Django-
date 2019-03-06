from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'payment'

urlpatterns = [
   url('^create_order/(?P<buying_option>[a-zA-Z0-9@#$&-]+)/$',views.create_order,name="create_order"),
]
