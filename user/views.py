from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from .models import User,Address
from .forms import RegisterUserForm,RegisterAddress


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
    if request.method == "POST":
        print("Successfully Received")
    return render(request,'user/contact_support.html')