#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Cash on 2019-08-23


from django.contrib import admin
from django.urls import path, include

from user import views

app_name = 'user'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login_view'),
]
