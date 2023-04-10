from django.db import models
from django.contrib.auth.models import User

from restaurant.models import Product

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete = models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    username = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    bio = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(default = 'default_user.jpg',null=True,blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.customer}'s Cart"
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"