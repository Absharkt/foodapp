from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'home.html')



def login(request):
    return render(request,'dclogin.html')


def signup(request):
    return render(request,'dcsignup.html')


def forgotpwd(request):
    return render(request,'forgotpwd.html')



def profile(request):
    return render(request,'profile.html')


def orders(request):
    return render(request,'orderss.html')


def itemss(request):
    return render(request,'itemss.html')



def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')