from django.urls import path
from . import views


urlpatterns = [
    path('rest_navbar',views.rest_base),
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.rest_login,name='login'),

    path('orders',views.orders,name='rest_orders'),
    path('order_details',views.order_details,name='order_details'),
    path('delivery_details',views.delivery_details,name='delivery_details'),
    path('categories',views.categories,name='categories'),

]