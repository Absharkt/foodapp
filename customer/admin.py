from django.contrib import admin
from . models import Customer,Cart,CartItem

# Register your models here.


admin.site.register(Customer)
admin.site.register(CartItem)
admin.site.register(Cart)