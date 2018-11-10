from django.shortcuts import render, redirect
from django import forms
from .models import User
from captcha.fields import CaptchaField
from django.utils import timezone
import hashlib


class UserForm(forms.Form):
    username = forms.CharField(label="用户名称", max_length=50, required=True)
    password1 = forms.CharField(label="用户密码", widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(label="确认密码", widget=forms.PasswordInput(), required=True)
    phone = forms.CharField(label="联系电话", max_length=20, required=True)
    email = forms.EmailField(label="联系邮件", max_length=50, required=True)
    address = forms.CharField(label="联系地址", widget=forms.Textarea, required=True)
    organization = forms.CharField(label="所属单位", max_length=100, required=True)
    code = CaptchaField(label="验证码", error_messages={"invalid": "验证码错误"})
    
    
class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    code = CaptchaField(label="验证码", error_messages={"invalid": "验证码错误"})


def regist(request):
    # Register View
    if request.session.get('is_login', None):
        return redirect("/index/")

    if request.method == "POST":
        register_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            phone = register_form.cleaned_data['phone']
            email = register_form.cleaned_data['email']
            address = register_form.cleaned_data['address']
            organization = register_form.cleaned_data['organization']
            print(password1)
            print(phone)
            print(email)
            if password1 != password2:
                message = "两次输入的密码不同！"
                return render(request, 'regist.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'regist.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'regist.html', locals())

                new_user = User.objects.create()
                new_user.username = username
                new_password = hash_code(password1)
                new_email = email
                new_phone = phone
                new_address = address
                new_organization = organization

                new_user.save()

                return redirect('/login/')

    register_form = UserForm()
    return render(request, 'regist.html', locals())


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        message = "所有字段都必须填写！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在"
        return render(request, 'login.html', locals())

    login_form = LoginForm()
    return render(request, 'login.html', locals())


def index(request):
    pass
    return render(request, 'index.html')


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index")

    request.session.flush()
    return redirect("/index/")


def hash_code(s, salt="mysite"):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()
