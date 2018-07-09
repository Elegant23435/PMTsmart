from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from wintop.permission import BasePermission
from stark.service import v1
from wintop import models



class CustomerConfig(BasePermission,v1.StarkConfig):

    def display_company_type(self,row=None,is_header=False):
        if is_header:
            return '公司行业类型'
        return row.get_company_type_display()

    def display_source(self,row=None,is_header=False):
        if is_header:
            return '客户来源'
        return row.get_source_display()

    def display_consult_business_type(self,row=None,is_header=False):
        if is_header:
            return '客户咨询业务项'
        return row.get_consult_business_type_display()

    def display_customer_rank(self,row=None,is_header=False):
        if is_header:
            return '客户级别'
        return row.get_customer_rank_display()

    def display_status(self,row=None,is_header=False):
        if is_header:
            return '客户状态'
        return row.get_status_display()



    # 显示字段
    list_display = ['company_name',display_company_type,display_source,'referral_from',display_consult_business_type,display_customer_rank,display_status,'consultant','negotiator_name','phone','email']

    # 搜索
    search_list = ['company_name__contains','consultant__name__contains']

    # 组合搜索
    comb_filter = ['status','consult_business_type','customer_rank','source','company_type']