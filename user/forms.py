from django import forms
from .models import User

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