#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: systemsgt.cn
@license: MIT Licence 
@contact: 18653076096@163.com
@site: http://www.systemsgt.cn
@software: PyCharm
@file: forms.py
@time: 2017/1/7 上午12:36
"""

from haystack.forms import SearchForm
from django import forms
from blog.models import Article, Category


class BlogSearchForm(SearchForm):
    querydata = forms.CharField(required=True)

    def search(self):
        datas = super(BlogSearchForm, self).search()
        if not self.is_valid():
            return self.no_query_found()

        if self.cleaned_data['querydata']:
            print(self.cleaned_data['querydata'])
        return datas
