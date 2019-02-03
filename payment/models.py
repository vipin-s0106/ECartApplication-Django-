from django.db import models
from user.models import Address,User

class OrderItem(models.Model):
    product_ids = models.CharField(max_length = 100)
    total_amount = models.FloatField()
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)