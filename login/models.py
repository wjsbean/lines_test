from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserInfo(AbstractUser):
    phone = models.CharField(verbose_name="联系电话", max_length=20)
    email = models.EmailField(verbose_name="联系邮件")
    company = models.CharField(verbose_name="工作单位", max_length=100)
    address = models.CharField(verbose_name="联系地址", max_length=200)
    #captcha = CaptchaField(label="验证码")

    def __str__(self):
        return self.username
