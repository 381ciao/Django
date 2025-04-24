from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import render, redirect,reverse
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST,require_GET
from .models import Blog,BlogComment,BlogCategory
from .forms import PubBlogForm
# Create your views here.
def blog_index(request):
    blogs = Blog.objects.all()
    return render(request,'index.html',context={'blogs':blogs})

def blog_detail(request,blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Exception as e:
        blog = None
    return render(request, 'blog_detail.html',context={'blog':blog})

# @login_required(login_url=reverse_lazy('csauth:login'))
# @login_required(login_url='/csauth/login/')
@login_required()
@require_http_methods(['GET','POST'])
def blog_pub(request):
    if request.method == 'GET':
        categoryies = BlogCategory.objects.all()
        return render(request, 'blog_pub.html',context={'categoryies':categoryies})
    else:
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            blog = Blog.objects.create(title=title,content=content,category_id=category_id,author=request.user)
            return JsonResponse({'code':200,'message':'博客发布成功', "data": {"blog_id": blog.id}})
        else:
            print(form.errors)
            return JsonResponse({'code':400,'message':'参数错误'})

@require_POST
@login_required()
def pub_comment(request):
    blog_id = request.POST.get('blog_id')
    content = request.POST.get('content')
    BlogComment.objects.create(blog_id=blog_id,content=content,author=request.user)
    # 重新加载博客详情页
    return redirect(reverse("blog:detail",kwargs={"blog_id": blog_id}))

@require_GET
def search_blog(request):
    # /search?q=xxx
    q = request.GET.get('q')
    blogs = Blog.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)).all()
    return render(request,'index.html',context={'blogs':blogs})