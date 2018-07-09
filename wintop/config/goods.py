#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:solo
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from wintop.permission import BasePermission
from stark.service import v1
from wintop import models



class GoodsConfig(BasePermission,v1.StarkConfig):

    def display_status(self,row=None,is_header=False):
        if is_header:
            return '阶段'
        return row.get_status_display()



    # 显示字段
    list_display = ['id','name','customer',display_status,'consultant']

    # 搜索
    search_list = ['name__contains','consultant__name__contains']


    # 组合搜索
    comb_filter = ['customer','status']