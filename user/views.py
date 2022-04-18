from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'home_menu.html')



def login(request):
    return render(request,'dclogin.html')


def signup(request):
    return render(request,'dcsignup.html')


def forgotpwd(request):
    return render(request,'forgotpwd.html')