from django.urls import path
from . import views


urlpatterns = [
    path('rest_navbar',views.rest_base),
    path('',views.home,name='home'),
    path('register',views.first_register,name='register0'),
    path('add_details',views.add_reg_details,name='register'),
    path('login',views.rest_login,name='login'),
    path('logout',views.rest_logout,name='logout'),

    path('orders',views.orders,name='rest_orders'),
    path('order_details',views.order_details,name='order_details'),
    path('delivery_details',views.delivery_details,name='delivery_details'),
    path('categories',views.categories,name='categories'),
    path('products/<str:id>',views.products,name='products'),

]