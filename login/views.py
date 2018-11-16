from django.shortcuts import render, redirect
from .models import UserInfo
from django.contrib.auth import login, logout, authenticate
from login.forms import MyUserCreationForm
from .forms import LoginForm, SetPassword
# Create your views here.

def registerView(request):
    if request.method == 'POST':
        user = MyUserCreationForm(request.POST)
        if user.is_valid():
            print("test")
            user.save()
            tips = "注册成功"
            user = MyUserCreationForm()
    else:
        tips = "注册不成功"
        user = MyUserCreationForm()
    return render(request, 'login/register.html', locals())


def loginView(request):
    title = "登录"
    unit_2 = "/login/register.html"
    unit_2_name = "立即注册"
    unit_1 = "/login/setpassword.html"
    unit_1_name = "修改密码"
    #if request.session.get('is_login', None):
    #    return redirect('/index/')

    if request.method == 'POST':
        login_form = LoginForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        if UserInfo.objects.filter(username = username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    request.session['is_login'] = True
                return render(request, 'login/index.html', locals())
            else:
                tips = "账号密码输入有误，请重新输入"
        else:
            tips = "用户不存在，请注册"

    login_form = LoginForm()
    return render(request, 'login/login.html', locals())

def setpasswordView(request):
    new_password = True
    if request.method == "POST":
        set_password = SetPassword()
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        if UserInfo.objects.filter(username=username):
            user = authenticate(username=username, password=old_password)
            user.set_password(new_password)
            user.save()
            tips = "密码修改成功"
        else:
            tips = "用户不存在"

    set_password = SetPassword()
    #return render(request, 'login/setpassword.html', locals())
    return render(request, 'main.html', locals())

def logoutView(request):
    logout(request)
    return redirect('/')

def index(request):
    username = request.user.username
    return render(request, 'login/index.html', locals())
