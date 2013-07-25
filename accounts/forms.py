#coding=utf-8

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Email:')
    username = forms.CharField(label='用户名:', max_length=30)
    password1 = forms.CharField(label='密码:', widget=forms.PasswordInput())
    password2 = forms.CharField(label='重复密码:', widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('Email已被占用')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('用户名已被占用')

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('密码与重复密码不一致')
