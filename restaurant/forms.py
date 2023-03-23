from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

from . models import Category,Restaurant,Product

class AddRestaurant(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateRestaurant(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ["user","image"]

class UpdateImage(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['image']

class AddProduct(ModelForm):
    class Meta:
        model = Product
        fields = ['title','description','price','image']


# class AddCategory(ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name']