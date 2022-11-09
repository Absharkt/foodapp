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
