from wintop.permission import BasePermission
from stark.service import v1
from wintop import models
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect

class UserInfoConfig(BasePermission,v1.StarkConfig):

    def display_gender(self,row=None,is_header=False):
        if is_header:
            return '性别'
        return row.get_gender_display()

    def display_stuff_position(self,row=None,is_header=False):
        if is_header:
            return '职位'
        return row.get_stuff_position_display()

    def display_education(self,row=None,is_header=False):
        if is_header:
            return '学历'
        return row.get_education_display()

    def display_id(self,row=None,is_header=False):
        if is_header:
            return '编号'
        return mark_safe("<a href='/user_detail/'>%s</a>" %(row.id,))



    # list_display = ['id','name','email',display_gender]
    list_display = [display_id,'name',display_gender,'depart',display_stuff_position,display_education,'graduation_school','major','date_joined','phone','email']

    # 搜索
    search_list = ['name__contains','major__contains','graduation_school__contains']

    # 组合搜索
    comb_filter = ['depart','stuff_position','gender', 'education']



    # 自定义视图函数
    def extra_url(self):
        patterns = [
            url(r'^user_detail/$', self.user_detail),
        ]
        return patterns

    def user_detail(self,request):
        current_user_id = request.session['user_info']['nid']
        current_user_id = 3
        detail_list = models.Customer.objects.filter(UserInfo=current_user_id)

        return render(request,'user_detail.html',{'detail_list':detail_list})