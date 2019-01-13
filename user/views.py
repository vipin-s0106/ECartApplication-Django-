from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from .models import User
from .forms import RegisterUserForm


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