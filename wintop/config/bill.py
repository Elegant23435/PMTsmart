#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:solo
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from wintop.permission import BasePermission
from stark.service import v1
from wintop import models



class BillConfig(BasePermission,v1.StarkConfig):

    def display_status(self,row=None,is_header=False):
        if is_header:
            return '阶段'
        return row.get_status_display()
    def display_bill(self,row=None,is_header=False):
        if is_header:
            return '单据类型'
        return row.get_bill_display()


    # 显示字段
    list_display = ['id','name','code','count','unit','goods','process','status','unqualified_name','stuff_approver','stuff_executor','stuff_drawer',display_bill,'date']
# ,'stuff_approver','stuff_executor','stuff_drawer'
    # 搜索
    search_list = ['name__contains','date__contains','stuff_executor__name__contains','stuff_drawer__name__contains']

    # 组合搜索
    comb_filter = ['goods','process','status','bill']
