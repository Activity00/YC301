#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年3月22日

@author: 武明辉
'''
from django.conf.urls import url

from fx import views

app_name='fx'

urlpatterns = [
    url(r'^$',view=views.index,name='index'),
    url(r'^getgra/$',view=views.getgra,name='getgra'),
]






