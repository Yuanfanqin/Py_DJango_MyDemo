# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from Demo1.models import Account, User, Skill, Color, Role
from .forms import account_signupForm, account_signinForm, account_reset_passwordForm
from random import Random
import time
import json


# Create your views here.
def page_signup(request):
    form = account_signupForm()
    return render(request, "Demo1/home.html", {'form': form});


def page_signin(request):
    form = account_signinForm()
    return render(request, "Demo1/login.html", {'form': form});


def page_reset_password(request):
    form = account_reset_passwordForm()
    return render(request, "Demo1/reset.html", {'form': form});


# 用户注册模块
def signup(request):
    if request.method == "POST":
        form = account_signupForm(request.POST)
        if form.is_valid():
            # 此处添加获取手机号对应的验证码的Code
            verify = "123456"
            if User.objects.filter(mobile=form.cleaned_data["mobile"]):
                return HttpResponse(status=409)
            elif form.cleaned_data["verify"] != verify:
                return HttpResponse(status=404)
            elif form.cleaned_data["inviteCode"] != "abc123":
                # 邀请码存储于inviteCode表，未查到对应的邀请码则返回403
                return HttpResponse(status=403)
            else:
                # 此处添加在inviteCode表中删除对应的邀请码的代码
                u = User.objects.create(
                    name=form.cleaned_data["name"],
                    mobile=form.cleaned_data["mobile"]
                    )
                a = Account.objects.create(
                    user=u,
                    password=form.cleaned_data["password"],
                    token=random_str(12),
                    expire=int(time.time())+24 * 60 * 60
                )
                # Django序列化方法serializers.serialize("json", QuerySet)无法序列化models对象
                # 该方法可以序列化对象，但是包含依赖关系的models无法正确显示关联的对象，只能显示外键
                # result = json.dumps(model_to_dict(a))
                # 该方法在所有models下添加toJSON方法，判断当出现依赖关系时进一步调用toJSON
                # 可以正确的序列化models对象，但是需要在每个model下添加该方法，待改进...
                result = a.toJSON()
                return HttpResponse(result, content_type='application/javascript')
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse()


# 用户登录模块
def signin(request):
    if request.method == "POST":
        form = account_signinForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(mobile=form.cleaned_data["mobile"]) or not Account.objects.filter(user__mobile=form.cleaned_data["mobile"],password=form.cleaned_data["password"]):
                # 使用Session存储登录错误次数
                return HttpResponse(status=404)
            else:
                a = Account.objects.get(user__mobile=form.cleaned_data["mobile"],password=form.cleaned_data["password"])
                result = a.toJSON()
                return HttpResponse(result, content_type='application/javascript')
        else:
             return HttpResponse(status=400)
    else:
        return HttpResponse()


# 用户token登录模块
def user(request):
    return HttpResponse()


# 用户修改密码模块
def reset_password(request):
    if request.method == "POST":
        form = account_reset_passwordForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(mobile=form.cleaned_data["mobile"]):
                return HttpResponse(status=400)
            else:
                # 此处添加调用API获取短信验证码的Code
                verify = "123456"
                if verify == form.cleaned_data["verify"]:
                    a = Account.objects.get(user__mobile=form.cleaned_data["mobile"])
                    a.password = form.cleaned_data["password"]
                    a.save()
                    result = a.toJSON()
                    return HttpResponse(result, content_type='application/javascript')
                else:
                    return HttpResponse(status=404)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse()



# 随机生成有字母与数字构成的字符串
# param:
#     int randomlength:生成字符串的长度
# return
#     string
def random_str(randomlength):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str
