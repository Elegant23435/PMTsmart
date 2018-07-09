#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:solo
from django.forms import Form
from django.forms import fields
from django.forms import widgets

class LoginForm(Form):
    user = fields.CharField(
        label='用户名',
        required=True,
        error_messages={
            'required':'用户名不能为空'
        },
        widget=widgets.TextInput(attrs={'class':'form-control'})
    )
    pwd = fields.CharField(
        label='密码',
        required=True,
        error_messages={
            'required': '密码不能为空'
        },
        widget=widgets.PasswordInput(attrs={'class':'form-control'})
    )