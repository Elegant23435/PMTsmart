#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:solo
from stark.service import v1
from wintop import models
from wintop.config import department
from wintop.config import userinfo
from wintop.config import customer
from wintop.config import goods
from wintop.config import customerfollowup
from wintop.config import component
from wintop.config import bill




v1.site.register(models.Department,department.DepartMentConfig)
v1.site.register(models.UserInfo,userinfo.UserInfoConfig)
v1.site.register(models.Customer,customer.CustomerConfig)
v1.site.register(models.Goods,goods.GoodsConfig)
v1.site.register(models.CustomerFollowUp,customerfollowup.CustomerFollowUpConfig)
v1.site.register(models.Component,component.ComponentConfig)
v1.site.register(models.Bill,bill.BillConfig)


