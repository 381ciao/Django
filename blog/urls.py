from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('index',views.blog_index,name='index'),
    path('detail/<int:blog_id>',views.blog_detail,name='detail'),
    path('pub',views.blog_pub,name='pub'),
]