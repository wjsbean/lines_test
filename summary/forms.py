from django import forms
from .models import User
from captcha.fields import CaptchaField

class Register(forms.Form):
    '''
        用户注册
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                             "placeholder": "请输入用户名",
                                                             "value": "",
                                                             "required": "required",}),
                               max_length=50, error_messages={"required": "用户名不能为空",})
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                 "placeholder": "请输入密码",
                                                                 "value": "",
                                                                 "required": "required",}),
                               min_length=6, max_length=50,
                               error_messages={"required": "密码不能为空",})
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                  "placeholder": "请输入密码",
                                                                  "value": "",
                                                                  "required": "required", }),
                                min_length=6, max_length=50,
                                error_messages={"required": "密码不能为空", })
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                          "placeholder": "请输入联系电话",
                                                          "value": "",
                                                          "required": "required",}),
                            min_length=11, max_length=15,
                            error_messages={"required": "密码不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control",
                                                           "placeholder": "请输入邮箱地址",
                                                           "value": "",
                                                           "required": "required",}),
                             max_length=50, error_messages={"required": "联系邮箱不能为空",})
    address = forms.CharField(label="联系地址", widget=forms.Textarea, required=True)
    organization = forms.CharField(label="所属单位", max_length=100, required=True)
    captcha = CaptchaField()

    def clean(self):
        #验证验证码
        try:
            captcha_x = self.cleaned_data['captcha']
        except Exception as e:
            print('except: ' + str(e))
            raise forms.ValidationError("验证码输入不正确，请重新输入")

        #验证用户名
        try:
            username = self.cleaned_data['username']
        except Exception as e:
            print('except: ' + str(e))
            raise forms.ValidationError("请输入合理的注册账号")

        try:
            email = self.cleaned_data['email']
        except Exception as e:
            print('except: ' + str(e))
            raise forms.ValidationError('请输入正确的邮箱格式')

        #登录验证
        is_username_exist = User.objects.filter(username=username).exists()
        is_email_exist = User.objects.filter(email=email).exists()
        if is_username_exist or is_email_exist:
            raise forms.ValidationError("对不起，您输入的账号已被注册")

        try:
            password = self.cleaned_data['password']
        except Exception as e:
            print('except: ' + str(e))
            raise forms.ValidationError("请输入至少8位密码")

        return self.cleaned_data
