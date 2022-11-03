from django.shortcuts import render

# Create your views here.


def rest_base(request):
    return render(request,'restaurant/rest_base.html')


def home(request):
    return render(request,'restaurant/home.html')


def register(request):
    return render(request,'restaurant/register.html')


def rest_login(request):
    return render(request,'restaurant/login.html')


def orders(request):
    return render(request,'restaurant/rest_orders.html')


def delivery_details(request):
    return render(request,'restaurant/delivery_details.html')


def categories(request):
    return render(request,'restaurant/categories.html')


def order_details(request):
    return render(request,'restaurant/order_details.html')