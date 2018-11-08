from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect  
from django.template import RequestContext
from django import forms
from django.template.loader import get_template
from .models import User
import json
from captcha.fields import CaptchaField

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label="用户名称", max_length=50, required=True)
    password = forms.CharField(label="用户密码", widget=forms.PasswordInput(), required=True)
    phone = forms.CharField(label="联系电话", max_length=20, required=True)
    email = forms.EmailField(label="联系邮件", max_length=50, required=True)
    address = forms.CharField(label="联系地址", widget=forms.Textarea, required=True)
    organization = forms.CharField(label="所属单位", max_length=100, required=True)
    code = CaptchaField(label="验证码", error_messages={"invalid": "验证码错误"})
    
    
class LoginForm(forms.Form):
    username = forms.CharField(label="姓名", max_length=20, help_text="用户名/手机号码")
    password = forms.CharField(label="密码", widget=forms.PasswordInput(), help_text="密码")
    code = CaptchaField(label="验证码", error_messages={"invalid": "验证码错误"})

# Register
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # acquire data from forms
            username = request.POST['username']
            password = request.POST['password']
            phone = request.POST['phone']
            email = request.POST['email']
            address = request.POST['address']
            organization = request.POST['organization']
            message = "恭喜你注册成功"
            # add to database
            #User.objects.create(username=username, password=password)
        else:
            message = "请检查输入的字段内容"
    else:
        uf = UserForm()

    template = get_template("regist.html")
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context.flatten())
    response = HttpResponse(html)

    try:
        if username: response.set_cookie('username', username)
        if password: response.set_cookie('password', password)
    except:
        pass
    return response


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            try:
                user = User.objects.get(username=login_name)
                if user.password == login_password:
                    response = redirect('/')
                    request.session['username'] = user.username
                    request.session['password'] = user.password
                    return redirect('/')
                else:
                    message = '密码错误，请核对后重新登录'
            except:
                message = '目前无法登录'
        else:
            message = "请检查输入的字段内容"
    else:
        login_form = LoginForm()
    
    template = get_template('login.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context.flatten())
    response = HttpResponse(html)
    return response
        

def index(request):
    pass

def logout(request):
    pass