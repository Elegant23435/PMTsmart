#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:solo
from stark.service import v1
from wintop import models
from wintop.permission import BasePermission


class DepartMentConfig(BasePermission,v1.StarkConfig):



    # 显示字段
    list_display = ['id','title','manager','count']