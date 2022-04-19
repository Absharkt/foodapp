from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home_page"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('forgot_password',views.forgotpwd,name="forgotpwd"),
    path('profile',views.profile,name="profile"),
    path('orders',views.orders,name="orders"),
    path('items',views.items_list,name="items_list")




]