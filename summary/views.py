from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect  
from django.template import RequestContext
from django.template.loader import get_template
from django import forms
from django.contrib import messages
from captcha.fields import CaptchaField
from .models import User
from .forms import Register


# Create your views here.

    
    
class LoginForm(forms.Form):
    username = forms.CharField(label="姓名", max_length=20)
    password = forms.CharField(label="密码", widget=forms.PasswordInput())
    code = CaptchaField(label="验证码", error_messages={"invalid": "验证码错误"})

# Register
def regist(request):
   if request.session.get('is_login', None):
       return redirect("/index/")
   if request.method == "POST":
       register_form = Register(request.POST)
       message = "请检查填写的内容！"
       if register_form.is_valid():
           username = register_form.cleaned_data['username']
           password1 = register_form.cleaned_data['password1']
           password2 = register_form.cleaned_data['password2']
           phone = register_form.cleaned_data['phone']
           email = register_form.cleaned_data['email']
           address = register_form.cleaned_data['address']
           organization = register_form.cleaned_data['organization']
           
           if password1 == password2:
               message = "两次输入的密码不同"
               return render(request, 'regist.html', locals())
           else:
               ssuser = User.objects.filter(username=username)
               if ssuser:
                   message = "用户名已经存在，请重新选择用户"
                   return render(request, 'regist.html', locals())
               seuser = User.objects.filter(email=email)
               if seuser:
                   message = "邮箱地址已经被注册，请使用其他邮箱注册！"
                   return render(request, 'regist.html', locals())               
               new_user = User.objects.create()
               new_user.username = username
               new_user.password = password1
               new_user.phone = phone
               new_user.email = email
               new_user.address = address
               new_user.organization = organization
               
               new_user.save()
               return redirect('/login/')
   
   
    register_form = Register()
   return render(request, 'login.html', locals())    


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            try:
                user = User.objects.get(username=login_name)
                if user.password == login_password:
                    request.session['username'] = user.username
                    request.session['password'] = user.password
                    messages.add_message(request, messages.SUCCESS, '登陆成功')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '密码错误，请检查后再试一次')
            except:
                messages.add_message(request, messages.WARNING, '找不到用户')
        else:
            messages.add_message(request, messages.INFO, '请检查输入的字段内容')
    else:
        login_form = LoginForm()
    
    return render(request, 'login.html', locals())


def index(request, pid=None, del_pass=None):
    if 'username' in request.session:
        username = request.session['username']
        password = request.session['password']
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)

def logout(request):
    pass