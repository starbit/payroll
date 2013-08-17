# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms.util import ErrorList
from django.forms import ModelForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(error_messages = {'required': u'用户名不能为空诶童鞋～'},max_length = 10,min_length=8)
    password = forms.CharField(error_messages = {'required': u'密码不能为空诶少年～'},max_length = 16,min_length = 8,widget = forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("密码错误啦~")
        self.check_for_test_cookie()
        return self.cleaned_data


class GetPasswordForm(forms.Form):
    email = forms.EmailField(max_length = 75, widget = forms.TextInput())
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).count() != 1:
            raise forms.ValidationError("这个邮箱木有对应的帐号诶～")
        return email

class ChangePasswordForm(PasswordChangeForm):
    old_password  = forms.CharField(label="原密码", widget=forms.PasswordInput, error_messages = {'required': u'新密码不能为空哦', 'min_length':u'至少8个字符啦', 'max_length':u'最多16个字符啦'}, min_length = 8, max_length = 16)
    new_password1 = forms.CharField(label="新密码", widget=forms.PasswordInput, error_messages = {'required': u'新密码不能为空哦', 'min_length':u'至少8个字符啦', 'max_length':u'最多16个字符啦'}, min_length = 8, max_length = 16)
    new_password2 = forms.CharField(label="新密码确认", widget=forms.PasswordInput, error_messages = {'required': u'新密码不能为空哦', 'min_length':u'至少8个字符啦', 'max_length':u'最多16个字符啦'}, min_length = 8, max_length = 16)


class ResetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="新密码", widget=forms.PasswordInput, error_messages = {'required': u'新密码不能为空哦', 'min_length':u'至少8个字符啦', 'max_length':u'最多16个字符啦'}, min_length = 8, max_length = 16)
    new_password2 = forms.CharField(label="新密码确认", widget=forms.PasswordInput, error_messages = {'required': u'新密码不能为空哦', 'min_length':u'至少8个字符啦', 'max_length':u'最多16个字符啦'}, min_length = 8, max_length = 16)

