from rest_framework import serializers
from user.models import User
from product.models import Product

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