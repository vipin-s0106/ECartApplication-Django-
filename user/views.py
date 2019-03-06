from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from .models import User,Address
from .forms import RegisterUserForm,RegisterAddress
from django.core.mail import EmailMessage
import random


def user_login(request):
    form = RegisterUserForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product:home')
        else:
            messages.warning(request,'Invalid Username/Password')
            return redirect('user:user_login')
    context = {'form':form}
    return render(request,'user/login.html',context=context)



def user_logout(request):
    logout(request)
    return redirect('product:home')


def register(request):
    form = RegisterUserForm(request.POST)
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    if User.objects.filter(username=username).count() == 0 and User.objects.filter(email=email).count() == 0 : 
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                message = "Hello "+request.user.name+"! You have successfully registered\n Username : "+username
                email = EmailMessage('Registeration Succesfull', message, to=[request.user.email])
                email.send()
                return redirect('product:home')
            else:
                messages.warning(request,'Some problem occurring contact Support Team No : 91XXXXXXXXX')
                return redirect('user:user_login')
        else:
            messages.warning(request,'Invalid Input Enter')
            return redirect('user:user_login')
    else:
        messages.warning(request, "User has already registered please login")
        return redirect('user:user_login')
    return redirect('product:home')


def manage_address(request):
    form = RegisterAddress()
    address_list = Address.objects.filter(user = request.user)
    if request.method == "POST":
        form = RegisterAddress( request.POST )
        address = form.save(commit = False)
        address.user = request.user
        address.save()
        return redirect('user:manage_address')
    context = {
        'form':form,
        'address_list':address_list,
        }
    return render(request,'user/manage_address.html',context=context)

def delete_address(request,address_id):
    Address.objects.filter(id = int(address_id)).first().delete()
    return redirect('user:manage_address')
    
def contact_support(request):
    message = ""
    if request.method == "POST":
        message = "\nName : "+request.POST['txtName']+"\nEmail :  "+request.POST['txtEmail']+"\n\nMessage : \n\n"+request.POST['txtMsg']
        email = EmailMessage('ECartSupport', message, to=['vipin.s0106@gmail.com'])
        email.send()
        message = "Success"
    context = {
        'message':message
        }
    return render(request,'user/contact_support.html',context=context)


def password_reset(request):
    if request.method == "POST":
        email = request.POST['email']
        if User.objects.filter(email=email).count() != 0:
            user = User.objects.filter(email=email).first()
            otp = random.randrange(100000,999999)
            request.session['otp'] = str(otp)
            request.session['email'] = email
            message = "Dear "+user.username+"\n\n"+str(otp)+" is your one time password(OTP).\nPlease enter the OTP to proceed.\n\nThank You\nTeam E-cart"
            mail = EmailMessage('ECart Password Reset', message, to=[email])
            mail.send()
            return redirect('user:password_reset_done')
        else:
            messages.warning(request, "Email: "+email+" has not been Registered")
            return redirect('user:user_login')
    return render(request,'user/password_reset.html') 
    
def password_reset_done(request):
    if request.method == "POST":
        if request.POST['otp'] == request.session['otp']:
            user = User.objects.filter(email=request.session['email']).first()
            print(user.password)
            user.set_password(request.POST['password'])
            user.save()
            del request.session['otp']
            del request.session['email']
            messages.info(request,"Your password has been changed successfully")
            return redirect('user:user_login')
        else:
            messages.warning(request,"You have entered the wrong otp")
            return redirect('user:password_reset_done')
    return render(request,'user/password_reset_done.html') 

def resend_otp(request):
    user = User.objects.filter(email=request.session['email']).first()
    otp = random.randrange(100000,999999)
    request.session['otp'] = str(otp)
    message = "Dear "+user.username+"\n\n"+str(otp)+" is your one time password(OTP).\nPlease enter the OTP to proceed.\n\nThank You\nTeam E-cart"
    mail = EmailMessage('ECart Password Reset', message, to=[request.session['email']])
    mail.send()
    return redirect('user:password_reset_done')
    
    
    
    
    
    
    
    
    
    
    