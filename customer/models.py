from django.db import models
from django.contrib.auth.models import User

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
