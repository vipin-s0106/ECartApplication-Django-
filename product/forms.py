from .models import ProductInfo
from django import forms
from usercart.models import Mycart

class CommentForm(forms.ModelForm):
    class Meta:
        model=ProductInfo
        fields=('reviews','rating','review_image2')
        widgets = {
            'reviews': forms.Textarea(attrs={'class': 'form-control','id':"reviews",'placeholder':"Enter reviews.."}),
            'rating': forms.NumberInput(attrs={'class': 'form-control','id':"reviews"}),
        }
        