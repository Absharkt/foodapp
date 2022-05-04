from django.shortcuts import render

# Create your views here.

def seller_form(request):
    return render(request,'seller_form.html')


def seller_menu(request):
    return render(request,'seller_menu.html')


def seller_orders(request):
    return render(request,'seller_orders.html')


def seller_order_details(request):
    return render(request,'seller_order_details.html')


def seller_dash(request):
    return render(request,'seller_dash.html')