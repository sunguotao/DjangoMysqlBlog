#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: systemsgt.cn
@license: MIT Licence
@contact: 18653076096@163.com
@site: http://www.systemsgt.cn
@software: PyCharm
@file: urls.py
@time: 2016/11/20 下午3:52
"""

from django.conf.urls import url
from django.contrib.auth import views as auth_view

from . import views
from .forms import LoginForm

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(success_url='/'), name='login', kwargs={'authentication_form': LoginForm}),
    url(r'^register/$', views.RegisterView.as_view(success_url="/"), name='register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout')
]
