from django.contrib import admin
from .models import UserInfo
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

@admin.register(UserInfo)
class UserInfoAdmin(UserAdmin):
    list_display = ['username', 'email', 'phone', 'company', 'address']
    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1] = (_('Personal info'),
                    {'fields': ('first_name', 'last_name', 'email',
                                'phone', 'company', 'address')})

