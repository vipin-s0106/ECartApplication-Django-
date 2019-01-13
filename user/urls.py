from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
   url('^login/$',views.user_login,name="user_login"),
   url('^logout/$',views.user_logout,name="user_logout"),
   url('^home/$',views.register,name="register")
]