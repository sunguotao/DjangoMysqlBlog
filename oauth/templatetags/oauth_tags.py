#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: systemsgt.cn
@license: MIT Licence 
@contact: 18653076096@163.com
@site: http://www.systemsgt.cn
@software: PyCharm
@file: oauth_tags.py
@time: 2017/3/4 下午3:22
"""
from oauth.oauthmanager import get_oauth_apps
from django.core.urlresolvers import reverse
from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('oauth/oauth_applications.html')
def load_oauth_applications(request):
    applications = get_oauth_apps()
    baseurl = reverse('oauth:oauthlogin')
    path = request.get_full_path()

    apps = list(map(lambda x: (x.ICON_NAME,
                               '{baseurl}?type={type}&next_url={next}'
                               .format(baseurl=baseurl, type=x.ICON_NAME, next=path)), applications))
    return {
        'apps': apps
    }
