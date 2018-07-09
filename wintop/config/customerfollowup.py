#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:solo
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from wintop.permission import BasePermission
from stark.service import v1
from wintop import models



class CustomerFollowUpConfig(BasePermission,v1.StarkConfig):

    def display_customer_rank(self,row=None,is_header=False):
        if is_header:
            return '客户级别'
        return row.get_customer_rank_display()

    def display_status(self,row=None,is_header=False):
        if is_header:
            return '客户状态'
        return row.get_status_display()

    def display_secrecy(self,row=None,is_header=False):
        if is_header:
            return '保密协议'
        return row.get_secrecy_display()


    # 显示字段
    list_display = ['customer',display_customer_rank,display_status,display_secrecy,'note','consultant','date']

    # 搜索
    search_list = ['customer__company_name__contains','consultant__name__contains']

    # 组合搜索
    comb_filter = ['status','secrecy','customer_rank']