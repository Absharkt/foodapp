from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base),

    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('cart',views.cart,name='cart'),
    path('orders',views.customer_orders,name='orders'),
    path('restaurents',views.restaurents,name='restaurents'),
    path('rest_home',views.rest_home,name='rest_home'),
    path('login',views.cust_login,name='cust_login'),
    path('register',views.cust_register,name='cust_register'),
    
]