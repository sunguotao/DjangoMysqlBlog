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
@time: 2016/11/12 下午3:03
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^postcomment/(?P<article_id>\d+)$', views.CommentPostView.as_view(), name='postcomment'),
    url(r'^article/(?P<article_id>\d+)/postcomment$', views.CommentPostView.as_view(), name='postcomment'),
]
