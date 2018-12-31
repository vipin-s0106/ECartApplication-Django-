from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#Creating Custom User Model here For Extra Fields Name,Mobile,birthdate
class User(AbstractUser):
    name = models.CharField(('Name'),max_length=100)
    mobile = models.IntegerField(('Mobile No'),null=True,unique=True,
                                 help_text=('Exclude +91 Extension'))
    birthdate = models.DateField(('Birth Date'),null=True,
                                 help_text=('Enter in "YYYY-MM-DD" format'),)
    
    def __str__(self):
        return self.name+" -- "+self.email
    
 

    
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(('Name'),null=False,max_length=300)
    street_address = models.TextField(('Street Address'),null=False)
    STATE_CHOICES = (
                    ('','--Select--'),
                    ('MAH', 'Mahashtra'),
                    ('RAJ', 'Rajsthan'),
                    ('GUJ', 'Gujrat'),
                    ('KAN', 'Karnataka'),
    )
    state_choice = models.CharField(('State'),max_length=5,
                                      choices=STATE_CHOICES,
                                      default='')
    pincode = models.IntegerField(('Pin-Code'),null=False)
    
    def __str__(self):
        return self.user.name+" -- "+str(self.pincode)
    
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    MODE_CHOICES = (
        ('','--Select--'),
        ('CARD','DEBIT CARD'),
        ('PAYTM','PAYTM'),
        ('UPI','UPI'),
        )
    payment_mode = models.CharField(('Payement Mode'),max_length=10,choices=MODE_CHOICES,default='')
    cardno = models.IntegerField(('Card No'),null=True,blank=True)
    paytmno = models.IntegerField(('Paytm No'),null=True,blank=True)
    upi = models.CharField(('UPI'),max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.user.name+" -- "+self.payment_mode
    
 
    