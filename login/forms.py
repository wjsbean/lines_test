from django.contrib.auth.forms import UserCreationForm
from .models import UserInfo
from django import forms

class MyUserCreationForm(UserCreationForm):
    #captcha = CaptchaField(label="验证码", error_messages={'invalid': "验证码错误"})
    class Meta(UserCreationForm.Meta):
        model = UserInfo
        fields = UserCreationForm.Meta.fields + (
            'phone', 'email', 'company', 'address')


class LoginForm(forms.Form):
    username = forms.CharField(label="名称",
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               max_length=50)
    password = forms.CharField(label="密码",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               max_length=50)
    #captcha = CaptchaField(label="验证码", error_messages={'invalid': "验证码错误"})


class SetPassword(forms.Form):
    username = forms.CharField(label="用户名称",
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               max_length=50)
    password = forms.CharField(label="原始密码",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               max_length=50)
    new_password = forms.CharField(label="新密码",
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                   max_length=50)