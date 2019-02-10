from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
   url('^login/$',views.user_login,name="user_login"),
   url('^logout/$',views.user_logout,name="user_logout"),
   url('^home/$',views.register,name="register"),
   url('^manage_address/$',views.manage_address,name="manage_address"),
   url('^delete_address/(?P<address_id>[0-9]+)/$',views.delete_address,name="delete_address"),
   url('^contact_support/$',views.contact_support,name="contact_support"),
]
