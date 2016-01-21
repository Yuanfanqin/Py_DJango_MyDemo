# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from Demo1.models import Account, User, Skill, Color, Role
from .forms import signupForm
from random import Random
import time;
import json


# Create your views here.
def index(request):
    form=signupForm()
    return render(request, "Demo1/home.html", {'form': form});


# def info(request):
#     if request.method == "POST":
#         form=regForm(request.POST)
#         if form.is_valid():
#             Person.objects.get_or_create(name=form.cleaned_data["name"],age=form.cleaned_data["age"])
#     else:
#         form=regForm()
#     return render(request, "Demo1/home.html", {'form': form})


# 用户注册模块
def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            if User.objects.filter(mobile=form.cleaned_data["mobile"]):
                return HttpResponse(status=409)
            else:
                u = User.objects.create(
                    name=form.cleaned_data["name"],
                    mobile=form.cleaned_data["mobile"]
                    )
                a = Account.objects.create(
                    user=u,
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
    return HttpResponse()


# 用户token登录模块
def user(request):
    return HttpResponse()


# 用户修改密码模块
def reset_password(request):
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
