import string
import random

from django.core.mail import send_mail
from django.http.response import JsonResponse
from django.shortcuts import render,redirect,reverse
from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm,LoginForm
from django.contrib.auth import get_user_model,login,logout


User = get_user_model()

# Create your views here.
@require_http_methods(["GET", "POST"])
def cs_login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remeber = form.cleaned_data.get('remeber')
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request, user)
                if not remeber:
                    request.session.set_expiry(0)
                return redirect(reverse('blog:index'))
            else:
                print('邮箱或密码错误！')
                return redirect(reverse('csauth:login'))

def cs_logout(request):
    logout(request)
    return redirect(reverse('blog:index'))

@require_http_methods(['POST','GET'])
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            User.objects.create_user(email=email, username=username, password=password)
            return redirect(reverse('csauth:login'))
        else:
            print(form.errors)
            # return render(request,'register.html',{'form':form})
            return redirect(reverse('csauth:register'))

def email_captcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({"code":400,"message":'必须传统邮箱！'})
    captcha = "".join(random.sample(string.digits,4))
    print(captcha)
    CaptchaModel.objects.update_or_create(email=email,defaults={'captcha':captcha})
    send_mail("出生定能注册验证码",message=f"你的出生验证码是：{captcha}",from_email=None,recipient_list=[email])
    return JsonResponse({"code":200,"message":"验证码发送成功！"})