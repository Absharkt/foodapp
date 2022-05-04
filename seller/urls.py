from django.urls import path
from . import views

urlpatterns = [
    path('',views.seller_form,name="form"),
    path('s-menu',views.seller_menu,name="s-menu"),
    path('s-orders',views.seller_orders,name="s-orders"),
    path('s-order-details',views.seller_order_details,name="s-order-details"),
    path('s-dashboard',views.seller_dash,name="s-dashboard")




]


