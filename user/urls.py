from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

app_name = 'user'

urlpatterns = [
   url('^login/$',views.user_login,name="user_login"),
   url('^logout/$',views.user_logout,name="user_logout"),
   path('password-reset/',views.password_reset,name="password_reset"),
   path('password_reset_done/',views.password_reset_done,name="password_reset_done"),
   path('resend_otp/',views.resend_otp,name="resend_otp"),
   url('^home/$',views.register,name="register"),
   url('^manage_address/$',views.manage_address,name="manage_address"),
   url('^delete_address/(?P<address_id>[0-9]+)/$',views.delete_address,name="delete_address"),
   url('^contact_support/$',views.contact_support,name="contact_support"),
]
