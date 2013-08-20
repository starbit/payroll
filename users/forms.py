# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms.util import ErrorList
from django.forms import ModelForm
from users.models import Leave, UserProfile

class LeaveForm(forms.ModelForm):
    date = forms.DateField(label=u"请假日期")

    class Meta:
        model = Leave
        exclude = ['user']

class LoginForm(AuthenticationForm):
    username = forms.CharField(error_messages = {'required': u'用户名不能为空哦少侠～'})
    password = forms.CharField(error_messages = {'required': u'密码不能为空哦少侠～'},widget = forms.PasswordInput)
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
    old_password  = forms.CharField(label="原密码", widget=forms.PasswordInput, error_messages = {'required': u'新密码不能为空哦'})
    new_password1 = forms.CharField(label="新密码", widget=forms.PasswordInput, error_messages = {'required': u'新密码不能为空哦'})
    new_password2 = forms.CharField(label="新密码确认", widget=forms.PasswordInput, error_messages = {'required': u'新密码不能为空哦'})


class ResetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="新密码", widget=forms.PasswordInput, error_messages = {'required': u'新密码不能为空哦'})
    new_password2 = forms.CharField(label="新密码确认", widget=forms.PasswordInput, error_messages = {'required': u'新密码不能为空哦'})
TOPIC=(
       ('ux','用户体验'),
       ('bug','有bug!'),
       ('suggestion','建议'),
       )

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC,label="主题")
    message = forms.CharField(widget=forms.Textarea(),label="内容",error_messages = {'required': u'内容为空？元芳，这不科学。'})
    sender = forms.EmailField(required=False,label="联系邮箱")
    def clean_message(self):
        message = self.cleaned_data.get('message','')
        if len(message) < 8:
            raise forms.ValidationError("元芳多说一点别那么小气啦!")
        return message

class ChangeUserProfile(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'payment_method', 'bank_account', 'mailing_address',)
