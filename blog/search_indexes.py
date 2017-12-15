#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: systemsgt.cn
@license: MIT Licence 
@contact: 18653076096@163.com
@site: http://www.systemsgt.cn
@software: PyCharm
@file: search_indexes.py
@time: 2017/1/7 上午12:44
"""
from haystack import indexes
from django.conf import settings
from blog.models import Article, Category, Tag


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    # title = indexes.CharField(document=True, use_template=True)
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(status='p')


"""
class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
    name = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(status='p')
"""
