#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: systemsgt.cn
@license: MIT Licence 
@contact: 18653076096@163.com
@site: http://www.systemsgt.cn
@software: PyCharm
@file: create_testdata.py
@time: 2017/3/11 上午1:58
"""

from django.core.management.base import BaseCommand
from blog.models import Article, Tag, Category
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
import datetime


class Command(BaseCommand):
    help = 'create test datas'

    def handle(self, *args, **options):
        user = \
            get_user_model().objects.get_or_create(email='test@test.com', username='testuser',
                                                   password='test!q@w#eTYU')[0]

        pcategory = Category.objects.get_or_create(name='pcategory', parent_category=None)[0]

        category = Category.objects.get_or_create(name='category', parent_category=pcategory)[0]

        category.save()

        for i in range(1, 10):
            article = Article.objects.get_or_create(category=category,
                                                    title='nice title ' + str(i),
                                                    body='nice content ' + str(i),
                                                    author=user
                                                    )[0]
            tag = Tag()
            tag.name = "nicetag" + str(i)
            tag.save()
            article.tags.add(tag)
            article.save()

        from DjangoBlog.utils import cache
        cache.clear()
        self.stdout.write(self.style.SUCCESS('created test datas \n'))
