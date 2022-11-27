from django.shortcuts import render,redirect
from . models import Restaurant,Category,Product
from . forms import AddRestaurant

from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . decorators import allowed_users

# Create your views here.


def rest_base(request):
    return render(request,'restaurant/rest_base.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['seller'])
def home(request):
    return render(request,'restaurant/home.html')



def first_register(request):
    #redirecting logged in users into the homepage without d login page
    if request.user.is_authenticated:
        return redirect('home')

    else:
        form = AddRestaurant

        if request.method == 'POST':
            form = AddRestaurant(request.POST)

            if form.is_valid():
                user = form.save()

                group = Group.objects.get(name = 'seller')
                user.groups.add(group)

                Restaurant.objects.create(
                    user = user,
                    name = user.username,
                    email = user.email,
                    phone = 91,
                    location = 'Add Location',
                    city = 'Add City')

                return redirect('login')
                
        values = {'form':form}
    return render(request,'restaurant/initial_reg.html',values)


@login_required(login_url='login')
@allowed_users(allowed_roles=['seller'])
def add_reg_details(request):
    return render(request,'restaurant/register.html')


def rest_login(request):
    #redirecting logged in users into the homepage without display login page
    if request.user.is_authenticated:
        return redirect('home')

    else:

        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request,username = username,password = password)

            if user is not None:
                login(request,user)
                return redirect('home')

            else:
                messages.info(request,'Username or Password is Incorrect..')

    return render(request,'restaurant/login.html')


def rest_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['seller'])
def orders(request):
    return render(request,'restaurant/rest_orders.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['seller'])
def delivery_details(request):
    return render(request,'restaurant/delivery_details.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['seller'])
def categories(request):
    # form = AddCategory

    if request.method == 'POST':

        name = request.POST['name']
        rest = Restaurant.objects.get(id = request.user.restaurant.id)
        catg=Category(restaurant = rest,name = name)
        catg.save()

    catgs = request.user.restaurant.category_set.all()

    context = {'categories':catgs}
    return render(request,'restaurant/categories.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['seller'])
def order_details(request):
    return render(request,'restaurant/order_details.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['seller'])
def products(request,id):
    catg = Category.objects.get(id=id)
    rest_id = request.user.restaurant
    print(rest_id)

    if request.method == 'POST':
        category = Category.objects.get(id=id)
        title = request.POST['name']
        img = request.FILES['img']
        desc = request.POST['desc']
        price = request.POST['price']

        product = Product(restaurant = rest_id,category = category,title = title,image = img,description = desc,price = price)
        product.save()

    all_products = Product.objects.filter(category=id)
        

    context = {'category':catg,'products':all_products}
    return render(request,'restaurant/cat_prods.html',context) 