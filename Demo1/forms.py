from django import forms
from django.core import validators


class signupForm(forms.Form):
    Client_Brand=forms.CharField(label="设备品牌")
    Client_Device=forms.CharField(label="设备型号")
    Client_OS=forms.CharField(label="操作系统")
    Client_Version=forms.CharField(label="牛咖版本号")
    mobile=forms.CharField(label="手机号",validators=[validators.RegexValidator(r'1\d{10}')])
    verify=forms.CharField(label="验证码",validators=[validators.RegexValidator(r'\d{6}')])
    name=forms.CharField(label="昵称",validators=[validators.RegexValidator(r'[＼x80-＼xffa-zA-Z][＼x80-＼xffa-zA-Z0-9]{3,19}')])
    password=forms.CharField(label="密码",validators=[validators.RegexValidator(r'[a-zA-Z0-9]{6,20}')])
    inviteCode=forms.CharField(label="邀请码",validators=[validators.RegexValidator(r'\w{6}')])