from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from .views import *
from . import views

app_name = 'rest_app'

'''
Router urls will provide you extra functionality like create view delete by writing only one 
viewSet below CustomerViewSet is wriiten using that we can create, delete,get customer details
'''

router = routers.DefaultRouter()
router.register('all_customer',CustomerViewSet)
router.register('all_customer_all_attribute',CustomerViewSet1)
router.register('all_products',ProductViewSet)

urlpatterns = [
   url('api/',include(router.urls)),
   url('^api/allProducts/$',get_allProduct),
   url('^api/product_detail/(?P<id>[0-9]+)/$',get_Product_deails),
   url('^class_based_api/allProducts/$',ProductAPIView.as_view()),
   path('class_based_api/product_detail/<int:id>/',ProductDetailAPIView.as_view()),

   url('^generics_api/product/$',ProductListView.as_view()),
   path('generics_api/product/<int:id>/',ProductListView.as_view()),

   #Urls for TokenAuthentication so url will be for login and logout
   path('api/login/',LoginView.as_view()),
   path('api/logout/',LogoutView.as_view()),

   #Urls for Django Rest Filtering Condition
   url('^filter_api/getProduct/$',GetProductHasPriceLessThan500.as_view()),
]