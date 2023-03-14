from django.shortcuts import render,redirect
from . forms import CreateCustomer
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . decorators import allowed_users

from . models import Customer
from restaurant.models import Restaurant,Category,Product
# Create your views here.


def base(request):
    return render(request,'customer/base.html')


@login_required(login_url='cust_login')
@allowed_users(allowed_roles=['customer'])
def home(request):
    restaurants = Restaurant.objects.all()

    context = {'rests':restaurants}
    return render(request,'customer/home.html',context)


@login_required(login_url='cust_login')
@allowed_users(allowed_roles=['customer'])
def profile(request):
    return render(request,'customer/cust_profile.html')


@login_required(login_url='cust_login')
@allowed_users(allowed_roles=['customer'])
def cart(request):
    return render(request,'customer/cart.html')


@login_required(login_url='cust_login')
@allowed_users(allowed_roles=['customer'])
def customer_orders(request):
    return render(request,'customer/orders.html')


@login_required(login_url='cust_login')
@allowed_users(allowed_roles=['customer'])
def restaurants(request):
    rest = Restaurant.objects.all()

    context = {'restaurant':rest}
    return render(request,'customer/restaurents.html',context)


@login_required(login_url='cust_login')
@allowed_users(allowed_roles=['customer'])
def rest_home(request,id):
    rest = Restaurant.objects.get(id=id)
    print(rest.id)
    
    categories = rest.category_set.all()
    print(categories)

    # products = rest.product_set.all()  not need
    # print(products)

    context = {'restaurant':rest,'categories':categories}
    return render(request,'customer/rest_home.html',context)


def cust_login(request):
    if request.user.is_authenticated:
        return redirect('cust_home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request,username = username,password = password)

            if user is not None:
                login(request,user)
                return redirect('cust_home')
            else:
                messages.info(request,'Username or Password is Incorrect..')


    return render(request,'customer/cust_login.html')


def cust_logout(request):
    logout(request)
    return redirect('cust_login')


def cust_register(request):
    #redirecting logged in users into the homepage without display login page

    if request.user.is_authenticated:
        return redirect('cust_home')
    else:
        form = CreateCustomer

        if request.method == 'POST':
            form = CreateCustomer(request.POST)

            if form.is_valid():
                user = form.save()

                group = Group.objects.get(name = 'customer')
                user.groups.add(group)

                Customer.objects.create(
                    user = user,
                    name = user.first_name,
                    username = user.username,
                    email = user.email,
                    phone = 91)

                return redirect('cust_login')

        
    return render(request,'customer/cust_reg.html',{'form':form})