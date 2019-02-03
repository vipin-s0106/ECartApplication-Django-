from django.db import models

# Create your models here.
from user.models import User
from product.models import Product
import datetime

class Mycart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.CharField(max_length=50,null=True,blank=True)
    
    
    
    def __str__(self):
        return self.user.name+" -- "+self.product.name
    
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name+" -- "+self.product.name
    
class Payment(models.Model):
    transaction_id = models.AutoField(primary_key=True,default=1000)
    transaction_type = models.CharField(max_length=150)
    transaction_amount = models.FloatField()
    payment_status = models.CharField(max_length=150)
    
    def __str__(self):
        return self.transaction_id+" -- "+self.transaction_amount
    
    
class MyOrder(models.Model):
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,null = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.CharField(max_length=50,null=True,blank=True)
    order_date = models.CharField(max_length=15,default=datetime.datetime.now().strftime('%Y-%m-%d'))
    deliver_date = models.CharField(max_length=15)
    unit_price = models.FloatField()
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.user.name+" -- "+self.product.name
    
    
    