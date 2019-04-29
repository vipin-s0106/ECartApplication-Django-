from rest_framework import serializers
from user.models import User
from product.models import Product
from rest_framework import exceptions
from django.contrib.auth import authenticate

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'email',
            'mobile',
            'birthdate'
        ]

class CustomerSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    #we are not using Model Serialzer so we have to write down the field
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        username = data.get("username","")
        password = data.get("password","")
        if username and password:
            user = authenticate(username = username,password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg="Account is Deactivated"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password"
            raise exceptions.ValidationError(msg)
        return data