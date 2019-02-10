from django import forms
from .models import User,Address

class RegisterUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('name','username','mobile','email','password')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','id':"name",'placeholder':"Enter Name.."}),
            'username': forms.TextInput(attrs={'class': 'form-control','id':"username",'placeholder':"Enter Username.."}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control','id':"mobile",'placeholder':"Enter Mobile.."}),
            'email': forms.EmailInput(attrs={'class': 'form-control','id':"email",'placeholder':"Enter Email.."}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','id':"password",'placeholder':"Enter Password.."}),
        }
        
        
class RegisterAddress(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ('name','street_address','state_choice','pincode')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','id':"name",'placeholder':"Enter Name.."}),
            'street_address': forms.Textarea(attrs={'class': 'form-control','id':"street_address",'placeholder':"Enter street_address.."}),
            'state_choice': forms.Select(attrs={'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control'})
        }