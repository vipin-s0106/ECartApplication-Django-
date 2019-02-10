from django.db import models
from user.models import Address,User
from datetime import datetime,timedelta

class OrderItem(models.Model):
    product_ids_details = models.CharField(max_length = 100)
    total_amount = models.FloatField()
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=150,default='cod')
    order_date = models.CharField(max_length=15,default=datetime.now().strftime('%Y-%m-%d'))
    deliver_date = models.CharField(max_length=15,default=(datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'))
    status = models.CharField(max_length=15,default="Order Placed")
    
    def __str__(self):
        return self.product_ids_details+" - "+str(self.total_amount)
    
