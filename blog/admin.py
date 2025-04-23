from django.contrib import admin
from .models import Blog,BlogComment,BlogCategory
# Register your models here.

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','category','content','pub_time','author']

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['blog','content','author','pub_time']

admin.site.register(BlogCategory,BlogCategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogComment,BlogCommentAdmin)