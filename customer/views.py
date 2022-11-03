from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request,'customer/base.html')


def home(request):
    return render(request,'customer/home.html')


def profile(request):
    return render(request,'customer/profile.html')


def cart(request):
    return render(request,'customer/cart.html')


def customer_orders(request):
    return render(request,'customer/orders.html')


def restaurants(request):
    return render(request,'customer/restaurents.html')


def rest_home(request):
    return render(request,'customer/rest_home.html')


def cust_login(request):
    return render(request,'customer/cust_login.html')


def cust_register(request):
    return render(request,'customer/cust_reg.html')