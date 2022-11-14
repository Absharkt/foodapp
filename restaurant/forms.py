from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

from . models import Category

class AddRestaurant(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


# class AddCategory(ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name']