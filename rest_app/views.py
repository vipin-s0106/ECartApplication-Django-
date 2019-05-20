from django.shortcuts import render,redirect
from product.models import Product,ProductInfo,Clothing,Accessories,Electronics,Footwear
from rest_framework import viewsets
from user.models import User
from .serializers import CustomerSerializer,CustomerSerializer1,ProductSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins

from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter

# Create your views here.
'''
Example of ViewSet
If we inherit GenericViewSet then we have to specify the mixins and models like 228 below code line
If we only inherit ViewSet then we have to specify the get post put delete method like 145 code line
If we inherit ModelViewSet then we have to just give the queryset and Serialzer class everything will handle by router
'''

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer


class CustomerViewSet1(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer1


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

'''
********  function based rest api ********
GET:
get method for getting the response


POST:
A HTTP.POST method always creates a new resource on the server
http post method is like a INSERT query in SQL which always creates a new record in database.

PUT:
In HTTP.PUT method the resource is first identified from the URL and if it exists then 
it is updated otherwise a new resource is created. When the target resource exists it 
overwrites that resource with a complete new body. That is HTTP.PUT method is used to CREATE or UPDATE a resource.
http put method is like a MERGE query in SQL which inserts or updates a record depending upon whether the given record exists.

PATCH:
A HTTP.PATCH method is used for partial modifications to a resource i.e. delta updates.
http patch method is like a UPDATE query in SQL which sets or updates selected columns only and not the whole row.

'''




#for doing POST method we will be required csrf token but this is rest api
# we don't have the csrf token so for that we have to use csrf_exempt decorator to avoid to method check for csrf_token
#use this is functionality by views during request.POST method

@csrf_exempt
def get_allProduct(request):
    if request.method == 'GET':
        products = Product.objects.all()

        #here when we pass the Resultset then we have to mention the many=True
        serialzer = ProductSerializer(products, many=True)

        #It will return the JsonResponse it is list of dictionary so when we convert the list of data in
        # Json then using safe=False we have to tell that this is Json response you can render it
        return JsonResponse(serialzer.data,safe=False)
    elif request.method == 'POST':
        #in order to test the rest api we have to use the Postman tool for Post Method

        #in request.POST we will have the dictionary we have to parse the Dictionary in Json Format Data
        # for that we will use JsonParser of rest_framework.parser
        data = JSONParser().parse(request)

        serailzer = ProductSerializer(data=data) # when we have to create new data then we have to pass like data=data
        # if you want to update something you have to pass like (data, data={'updated_column_name'='updated_value'}, partial=True)
        #here partial=True is written bcz if you don't write for update even you have to provide all required columns

        if serailzer.is_valid():
            serailzer.save()
            return JsonResponse(serailzer.data, status=201) # 201 is for creating object 200 successfully update the object
        return JsonResponse(serailzer.errors, status = 400)

@csrf_exempt
def get_Product_deails(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({"error":"Given question object not found."},status=404)
    if request.method == 'GET':
        #here when we pass the Resultset then we have to mention the many=True
        serialzer = ProductSerializer(product)

        #here it is Json response so we don't required to tell that this is Json bcz it already in json
        return JsonResponse(serialzer.data)
    elif request.method == 'PUT':
        #in order to test the rest api we have to use the Postman tool for Post Method

        #in request.POST we will have the dictionary we have to parse the Dictionary in Json Format Data
        # for that we will use JsonParser of rest_framework.parser
        data = JSONParser().parse(request)
        serailzer = ProductSerializer(product,data=data,partial=True) # when we have to create new data then we have to pass like data=data
        # if you want to update something you have to pass like (data, data={'updated_column_name'='updated_value'}, partial=True)
        #here partial=True is written bcz if you don't write partial =True then for update you have to provide all required columns

        if serailzer.is_valid():
            serailzer.save()
            return JsonResponse(serailzer.data, status=200) # 201 is for creating object 200 successfully update the object
        return JsonResponse(serailzer.errors, status = 400)
    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({"message":"Done"},status=200)
    elif request.method == 'PATCH':
        # in order to test the rest api we have to use the Postman tool for Post Method

        # in request.POST we will have the dictionary we have to parse the Dictionary in Json Format Data
        # for that we will use JsonParser of rest_framework.parser
        data = JSONParser().parse(request)

        serailzer = ProductSerializer(product, data=data,partail=True)

        if serailzer.is_valid():
            serailzer.save()
            return JsonResponse(serailzer.data,
                                status=200)  # 201 is for creating object 200 successfully update the object
        return JsonResponse(serailzer.errors, status=400)


'''
Class Based View
'''

#this class is for to getting data and Creating data
class ProductAPIView(APIView):
    # for post method it will accept Json data so we don't have to parse in Json like in method based api
    def get(self,request):
        products = Product.objects.all()
        serialzer = ProductSerializer(products, many=True)
        return Response(serialzer.data,status=210)

    def post(self,request):
        data = request.data
        serailzer = ProductSerializer(data=data)

        if serailzer.is_valid():
            serailzer.save()
            return Response(serailzer.data,
                                status=201)  # 201 is for creating object 200 successfully update the object
        return Response(serailzer.errors, status=400)

class ProductDetailAPIView(APIView):
    # for put method it will accept Json data so we don't have to parse in Json like in method based api
    def get_object(self,id):
        try:
            product = Product.objects.filter(id=id).first()
            if product == None:
                raise Exception
            return product
        except Exception as e:
            return Response({"error":"Given question object not found."},status=404)

    def get(self,request,id=None):
        product = self.get_object(id)
        serialzer = ProductSerializer(product)
        return Response(serialzer.data)


    def put(self,request,id=None):
        product = self.get_object(id)
        data = request.data
        serailzer = ProductSerializer(product, data=data,
                                      partial=True)

        if serailzer.is_valid():
            serailzer.save()
            return Response(serailzer.data, status=200) # 201 is for creating object 200 successfully update the object
        return Response(serailzer.errors, status = 400)


    def delete(self, request,id=None):
        product = self.get_object(id)
        product.delete()
        return Response({"message": "Done"}, status=200)




'''
Build API view using generic api view
'''

'''
API is already build we have to just specify the serialzer class and queryset
'''

'''
in this we have to just specifiy the generics view and Different mixins for different operations

we have to provide the slug also like serializer class, queryset,lookup_field
lookup_field is required fro detailing purpose when work with single product
like put get of single product delete 

we have to overwrite that mixins method and use according to our requirement

POST method is not working just check out

perform_create method is called before completion of create method
this method will help if some extra things need to be saved like in method shown

same for peroform_update method

'''


class ProductListView(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'

    '''
    Adding Authentication classes and permission classes to
    access this api only with registered user/Admin User with this application
    permission type api can be tested using Postman using Autherization Tab
    '''

    #here first it will check first class authntication i.e. session based so it will check wheathere session_id is passed or not
    # if first method not provided then it will go for second one i.e. Username password
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    #we have to define permission classes to make it effective
    permission_classes = [IsAuthenticated]

    #permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        return self.list(request)

    def create(self,request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save()

        #serializer.save(created_by=self.request.user)

    def put(self,request,id=None):
        return self.update(request,id)

    def perform_update(self, serializer):
        serializer.save()

    def delete(self,request,id=None):
        return self.destroy(request,id)






'''
Token Authentication Related all views
'''
from .serializers import LoginSerializer
from django.contrib.auth import login,logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user=user)
        token,created = Token.objects.get_or_create(user=user)
        '''
        created will be true or false if new token get created then it will be true else
        it will be false
        '''
        return Response({"Token":token.key},status=200)



class LogoutView(APIView):
    #To check user is login or not so that we have to include TokenAuthentication
    authentication_classes = (TokenAuthentication,)

    def post(self,request):
        #here we have to logout only from client site if we logout from server then it will logout from all the application
        #where it is logged in so we will only use logout method
        logout(request)
        return Response({"Msg":"Successfully Logout"},status=204)



'''
Filter in Django Rest Framework

if you have multiple user in databse but you want only active user that can acieve using filter

Two to do the Filtering Condition
1 - In Query we can provide the Filter condition
2 - we can use third party libraries django-filter
'''

class GetProductHasPriceLessThan500(generics.ListAPIView):
    serializer_class = ProductSerializer


    '''
    1 method - Using Get Queryset
    '''
    #This queryset will be reading data from URL and putting into the Querset as filter condition


    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     price = self.request.query_params.get('price','')
    #     if price:
    #         queryset = queryset.filter(price__lte = int(price))
    #     return queryset


    '''
    2 method - Using Django Filter Third party libraries
    
    in second method it won't work for < condition it will only work for == condition take exmaple of 499.0
    
    '''
    queryset = Product.objects.all()

    filter_backends = (DjangoFilterBackend,OrderingFilter,SearchFilter)
    filter_fields = ('price',)

    '''
    Ordering Filter
    '''
    ordering_fields = ('name',)
    '''
    for testing we have to pass in url like  /filter_api/getProduct/?ordering=name
    '''

    '''
    Search Field
    '''
    search_fields = ('name',)
    '''
        for testing we have to pass in url like  /filter_api/getProduct/?search=pants
    '''
