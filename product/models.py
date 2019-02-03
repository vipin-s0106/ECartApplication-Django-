from django.db import models
from user.models import User
# Create your models here.
import datetime
from PIL import Image


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
    
    #Saving Image to required size
    '''
    def save(self,**kwargs):
        super().save()
        
        img1 = Image.open(self.product_image1.path)
        img2 = Image.open(self.product_image2.path)
        
        if img1.height > 300 or img1.width > 250:
            if img1.height > 300 and img1.width < 250:
                output_size = (300,img1.width)
            elif(img1.height < 300 and img1.width > 250):
                output_size = (img1.height,250)
                img1.thumbnail(output_size)
                img1.save(self.product_image1.path)
            else:
                output_size = (300,250)
            img1.thumbnail(output_size)
            img1.save(self.product_image1.path)
            
        if img2.height > 300 or img2.width > 250:
            if img2.height > 300 and img2.width < 250:
                output_size = (300,img2.width)
                
            elif(img2.height < 300 and img2.width > 250):
                output_size = (img2.height,250)
            else:
                output_size = (300,250)
            img2.thumbnail(output_size)
            img2.save(self.product_image2.path)
    '''        
            
        
    

class ProductInfo(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reviews = models.TextField(null=True,blank=True)
    rating = models.IntegerField(default=1)
    date = models.CharField(max_length=15,default=datetime.datetime.now().strftime('%Y-%m-%d'))
    review_image2 = models.FileField(("Attach image"),default="NoImage.png")
    
    
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
    
    def description_split(self):
        return self.description.split(";")
    
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
    
    def description_split(self):
        return self.description.split(";")
    

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
    size = models.CharField(max_length = 150,null=True,blank=True)
    color = models.CharField(max_length = 150,null=True,blank=True,help_text=('Please enter brand like - Red,brown etc'))
    
    
    def description_split(self):
        return self.description.split(";")
    
    def __str__(self):
        return self.product.name+" "+self.category+" "+self.gender
    

class Electronics(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    category = models.CharField(max_length = 150,null=False)
    sub_category = models.CharField(('Sub Category'),max_length = 150,null=False)
    description = models.TextField(null=False)
    brand = models.CharField(max_length = 150,null=True,blank=True)
    size = models.CharField(max_length = 150,null=True,blank=True)
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
    
    def description_split(self):
        return self.description.split(";")
    
    def __str__(self):
        return self.product.name+" | "+self.category+" | "+self.sub_category
    