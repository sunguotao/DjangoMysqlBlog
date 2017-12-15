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
@time: 2016/11/26 下午5:25
"""

from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    url(r'^oauth/authorize$', views.authorize),
    url(r'^oauth/requireemail/(?P<oauthid>\d+).html', views.RequireEmailView.as_view(), name='require_email'),
    url(r'^oauth/emailconfirm/(?P<id>\d+)/(?P<sign>\S+).html', views.emailconfirm, name='email_confirm'),
    url(r'^oauth/bindsuccess/(?P<oauthid>\d+).html', views.bindsuccess, name='bindsuccess'),
    url(r'^oauth/oauthlogin$', views.oauthlogin,name='oauthlogin')
]
