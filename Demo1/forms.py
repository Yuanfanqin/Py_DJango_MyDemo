from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class account_signupForm(forms.Form):
    Client_Brand = forms.CharField(label="设备品牌")
    Client_Device = forms.CharField(label="设备型号")
    Client_OS = forms.CharField(label="操作系统")
    Client_Version = forms.CharField(label="牛咖版本号")
    mobile = forms.CharField(label="手机号", validators=[validators.RegexValidator(r'1\d{10}')])
    verify = forms.CharField(label="验证码", validators=[validators.RegexValidator(r'\d{6}')],  help_text="邀请码：123456")
    name = forms.CharField(label="昵称", validators=[validators.RegexValidator(r'[＼x80-＼xffa-zA-Z][＼x80-＼xffa-zA-Z0-9]{3,19}')])
    password = forms.CharField(label="密码", validators=[validators.RegexValidator(r'[a-zA-Z0-9]{6,20}')], help_text="6-20位字母数字")
    inviteCode = forms.CharField(label="邀请码", validators=[validators.RegexValidator(r'\w{6}')],  help_text="邀请码：abc123")


class account_signinForm(forms.Form):
    Client_Brand = forms.CharField(label="设备品牌")
    Client_Device = forms.CharField(label="设备型号")
    Client_OS = forms.CharField(label="操作系统")
    Client_Version = forms.CharField(label="牛咖版本号")
    mobile = forms.CharField(label="手机号")
    password = forms.CharField(label="密码")


class account_reset_passwordForm(forms.Form):
    mobile = forms.CharField(label="手机号", validators=[validators.RegexValidator(r'1\d{10}')])
    password = forms.CharField(label="密码", validators=[validators.RegexValidator(r'[a-zA-Z0-9]{6,20}')])
    verify = forms.CharField(label="验证码", validators=[validators.RegexValidator(r'\d{6}')],  help_text="邀请码：abc123")
