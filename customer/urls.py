from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base),

    path('',views.home,name='cust_home'),
    path('profile',views.profile,name='profile'),
    path('cart',views.cart,name='cart'),
    path('orders',views.customer_orders,name='orders'),
    path('restaurants',views.restaurants,name='restaurants'),
    path('rest_home/<str:id>',views.rest_home,name='rest_home'),
    path('login',views.cust_login,name='cust_login'),
    path('logout',views.cust_logout,name='cust_logout'),
    path('register',views.cust_register,name='cust_register'),
    
]