from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home_page"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('forgot_password',views.forgotpwd,name="forgotpwd")
]