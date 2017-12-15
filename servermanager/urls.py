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
@time: 2017/8/27 上午2:27
"""

from django.conf.urls import url
from werobot.contrib.django import make_view
from .robot import robot

urlpatterns = [
    url(r'^robot/', make_view(robot)),

]
