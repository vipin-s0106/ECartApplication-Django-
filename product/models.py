from django.db import models
from user.models import User
# Create your models here.
import datetime

class Product(models.Model):
    name = models.CharField(max_length = 150)
    price = models.FloatField(null=False)
    offer = models.IntegerField(default=0)
    emi_discount = models.FloatField(default=0)
    card_discount = models.FloatField(default=0)
    avaiable_stock = models.IntegerField(default=10)
    visited = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    product_image1 = models.ImageField(null=True,blank=True)
    product_image2 = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return "ID : "+str(self.pk)+" -- "+self.name
    

class ProductInfo(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reviews = models.TextField(null=True,blank=True)
    rating = models.IntegerField(null=True,blank=True,help_text=('Please give rating out of 5'))
    review_image2 = models.ImageField(null=True,blank=True)
    
    
    def __str__(self):
        return self.product.name+" -- "+self.user.name
    
    
class Clothing(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    category = models.CharField(max_length = 150,null=False)
    sub_category = models.CharField(('Sub Category'),max_length = 150,null=False)
    description = models.TextField(null=False)
    GENDER_CHOICES = (
                     ('M', 'Male'),
                     ('F', 'Female'),
                     ('K','Kids')
                    )  
    gender = models.CharField('Gender',choices=GENDER_CHOICES,max_length=1,null=True,blank=True)
    brand = models.CharField(max_length = 150,null=True,blank=True)
    size = models.CharField(max_length = 150,null=True,blank=True,help_text=('Please enter size like - M,S,L etc'))
    color = models.CharField(max_length = 150,null=True,blank=True,help_text=('Please enter brand like - Red,brown etc'))
    
    def __str__(self):
        return self.product.name+" "+self.category+" "+self.gender
    
class Footwear(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    category = models.CharField(max_length = 150,null=False)
    sub_category = models.CharField(('Sub Category'),max_length = 150,null=False)
    description = models.TextField(null=False)
    GENDER_CHOICES = (
                     ('M', 'Male'),
                     ('F', 'Female'),
                     ('K','Kids')
                    )  
    gender = models.CharField('Gender',choices=GENDER_CHOICES,max_length=1,null=True)
    brand = models.CharField(max_length = 150,null=True,blank=True)
    size = models.CharField(max_length = 150,null=True,blank=True,help_text=('Please enter size like - M,S,L etc'))
    color = models.CharField(max_length = 150,null=True,blank=True,help_text=('Please enter brand like - Red,brown etc'))
    
    def __str__(self):
        return self.product.name+" "+self.category+" "+self.gender
    

class Accessories(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    category = models.CharField(max_length = 150,null=False)
    sub_category = models.CharField(('Sub Category'),max_length = 150,null=False)
    description = models.TextField(null=False)
    GENDER_CHOICES = (
                     ('M', 'Male'),
                     ('F', 'Female'),
                     ('K','Kids')
                    )  
    gender = models.CharField('Gender',choices=GENDER_CHOICES,max_length=1,null=True)
    brand = models.CharField(max_length = 150,null=True,blank=True)

class Electronics(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    category = models.CharField(max_length = 150,null=False)
    sub_category = models.CharField(('Sub Category'),max_length = 150,null=False)
    description = models.TextField(null=False)
    GENDER_CHOICES = (
                     ('M', 'Male'),
                     ('F', 'Female'),
                     ('K','Kids')
                    )  
    gender = models.CharField('Gender',choices=GENDER_CHOICES,max_length=1,null=True)
    brand = models.CharField(max_length = 150,null=True,blank=True)
    screen_size = models.CharField(max_length = 150,null=True,blank=True,help_text=('Please enter screen size like - 15.6,5.5 etc'))
    os = models.CharField(max_length = 150,null=True,blank=True)
    ram_size = (
                     ('','--Select--'),
                     ('4', '4 GB'),
                     ('8', '8 GB'),
                     ('16','16 GB')
                    ) 
    storage_choice = (
                     ('','--Select--'),
                     ('16', '16 GB'),
                     ('32', '32 GB'),
                     ('64','64 GB'),
                     ('128','128 GB'),
                     ('500','500 GB'),
                     ('1','1 TB'),
                     ('2','2 GB'),
        )
    camera_choice = (
                     ('','--Select--'),
                     ('1.2', '1.2 MP'),
                     ('2', '2 MP'),
                     ('5','5 MP'),
                     ('8','8 MP'),
                     ('12','12 MP'),
                     ('16','16 MP'),
                     ('20','20 MP'),
                     ('28','28 MP'),
        )
    ram = models.CharField(choices=ram_size,null=True,blank=True,default='',max_length=50)
    storage = models.CharField(choices=storage_choice,null=True,blank=True,default='',max_length=50)
    camera = models.CharField(choices=camera_choice,null=True,blank=True,default='',max_length=50)
    