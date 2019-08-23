#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Cash on 2019-08-23
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
