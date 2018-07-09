#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:solo
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from wintop.permission import BasePermission
from stark.service import v1
from wintop import models



class ComponentConfig(BasePermission,v1.StarkConfig):

    def display_status(self,row=None,is_header=False):
        if is_header:
            return '阶段'
        return row.get_status_display()



    # 显示字段
    list_display = ['id','name','code','count','unit','goods','process','status','unqualified_name','position']

    # 搜索
    search_list = ['name__contains','unqualified_name__contains','position__contains']
    #

    # 组合搜索
    comb_filter = ['goods','process','status']