from django.contrib import admin
from . models import Restaurant,Category,Product

# Register your models here.


admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Product)