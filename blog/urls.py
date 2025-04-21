from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('index',views.blog_index,name='index'),
]