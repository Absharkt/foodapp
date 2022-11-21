from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Restaurant(models.Model):
    user = models.OneToOneField(User,null = True,on_delete = models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    description = models.CharField(max_length=100,null=True,blank = True)
    location = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50,null=True)
    price = models.IntegerField(null=True)
    image = models.ImageField(default='download.jpg',null=True,blank=True)

    def __str__(self):
        return self.title
