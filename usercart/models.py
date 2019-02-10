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
    
    
    
    