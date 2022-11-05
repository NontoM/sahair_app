from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import transaction
from .forms import CustomerSignUpForm
from .models import User


def registerPage(request): 
    return render(request, '../templates/accounts/register.html', {})


@transaction.atomic
def customerRegisterView(request):
   #check if the current request from a user was performed using HTTP "POST" method
    if request.method == "POST" and request.POST['first_name'] and request.POST['last_name'] and request.POST['email'] and request.POST['username']  and request.POST['password1'] and request.POST['password2']:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username has been taken')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        if len(password) < 6:
            messages.error(request, 'Password should be atleast 6 characters.')
        if password != password2:
            messages.error(request, 'Password does not match.')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password, is_customer=1)
            if not user:
                messages.error(request, 'Account could not be created.')
                return redirect('customer_register')
            else:
                #new_customer.set_password(password)
                user.save()
                userlog = authenticate(username=username, password=password)
                
                if userlog is not None:
                    login(request, userlog)
                    if request.user.is_authenticated and request.user.is_customer:
                        return redirect('/')
        
    return render(request, '../templates/accounts/customer_register.html', {})

@transaction.atomic
def merchantRegisterView(request):
   #check if the current request from a user was performed using HTTP "POST" method
    if request.method == "POST" and request.POST['first_name'] and request.POST['last_name'] and request.POST['email'] and request.POST['username']  and request.POST['password1'] and request.POST['password2']:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username has been taken')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        if len(password) < 6:
            messages.error(request, 'Password should be atleast 6 characters.')
        if password != password2:
            messages.error(request, 'Password does not match.')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password, is_merchant=1)
            if not user:
                messages.error(request, 'Account could not be created.')
                return redirect('customer_register')
            else:
                #new_merchant.set_password(password)
                user.save()
                #messages.error(request, 'Account successfully registerd')
                userlog = authenticate(username=username, password=password)   
                if userlog is not None:
                    login(request, userlog)
                    if request.user.is_authenticated and request.user.is_merchant:
                        return redirect('/')
        
    return render(request, '../templates/accounts/merchant_register.html', {})

@transaction.atomic
def loginView(request):
    if request.method == 'POST' and request.POST['username']  and request.POST['password1']:
        username = request.POST['username']
        password = request.POST['password1']
        userlog = authenticate(username=username, password=password)
        if userlog is not None:
            login(request, userlog)
            if request.user.is_authenticated and request.user.is_customer:
                return redirect('/')
            elif request.user.is_authenticated and request.user.is_merchant:
                return redirect('/')
            else:
                messages.error(request,'Enter username and password')
                return redirect('login')
        else:
            messages.error(request, 'Incorrect login credentials')
            return redirect('login')
    
    return render(request, '../templates/accounts/login.html', {})



def log_out(request):
    logout(request)
    return redirect('/')
