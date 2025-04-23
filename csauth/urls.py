from django.urls import path
from . import  views

app_name = 'csauth'
urlpatterns = [
    path('login',views.cs_login,name='login'),
    path('register',views.register,name='register'),
    path('captcha',views.email_captcha,name='captcha'),
    path('logout',views.cs_logout,name='logout'),
]