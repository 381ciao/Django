import string
import random

from django.core.mail import send_mail
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import CaptchaModel

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def email_captcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({"code":400,"message":'必须传统邮箱！'})
    captcha = "".join(random.sample(string.digits,4))
    print(captcha)
    CaptchaModel.objects.update_or_create(email=email,defaults={'captcha':captcha})
    send_mail("出生定能注册验证码",message=f"你的出生验证码是：{captcha}",from_email=None,recipient_list=[email])
    return JsonResponse({"code":200,"message":"验证码发送成功！"})