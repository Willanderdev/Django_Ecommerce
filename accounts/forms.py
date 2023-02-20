# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name',
                  'image', 'is_active', 'is_staff']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'image', 'name']
