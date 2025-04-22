from django.shortcuts import render

# Create your views here.
def blog_index(request):
    return render(request,'index.html')

def blog_detail(request,blog_id):
    return render(request, 'blog_detail.html')

def blog_pub(request):
    return render(request, 'blog_pub.html')