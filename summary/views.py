from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from .models import User
import json

# Create your views here.


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=50)
    password = forms.CharField(label="密码", widget=forms.PasswordInput())

# Register
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # acquire data from forms
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # add to database
            User.objects.create(username=username, password=password)
            return HttpResponse('恭喜你，注册成功')
        else:
            uf = UserForm()
        return render_to_response('regist.html', {'uf':uf}, content_type=RequestContext(req))

# Login
def login(req):
    if req.method == 'POST':
        data = req.POST
        # 将传入的参数json话
        jstr = json.dumps(data)
        # 封装json然后获取其中的某个字段
        decodejson = json.loads(jstr)
        username = decodejson['username']
        print('username==%s' %username)
        # 将username存储到session中
        req.session['username'] = username
        responseData = {'state':0, 'msg':'success', 'username':username}
        return HttpResponse(json.dumps(responseData, ensure_ascii=False, encoding="utf-8"),
                            content_type="application/json")
    else:
        responseData = {'state':1, 'msg':'fail'}
        return render(req, 'login.html', json.dumps(responseData))

#Login success
def index(req):
    # 获取session中的username
    username = req.session.get('username', False)
    print(username)
    return render_to_response('index.html', {'username':username})

#Quit
def logout(req):
    response = HttpResponse('logout !!')
    # 清理cookie里保存的username
    response.delete_cookie('username')
    return response