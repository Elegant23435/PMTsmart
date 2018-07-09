from django.db import models
from rbac import models as rbac_model
from django.db import models

class Department(models.Model):
    '''部门信息表'''
    title = models.CharField(verbose_name='部门名称', max_length=16)
    manager = models.ForeignKey(to="UserInfo",verbose_name='部门经理', max_length=16)
    count = models.IntegerField(verbose_name=u'人数')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'部门信息表'
        verbose_name_plural = u"部门信息表"

class UserInfo(rbac_model.Userprofile):
    """员工信息表"""
    # nickname = models.CharField(verbose_name='昵称', max_length=32,default=None)
    email = models.EmailField(verbose_name='邮箱', max_length=255, unique=True)
    phone = models.BigIntegerField(verbose_name=u'手机号', unique=True)
    gender_choices = ((1, '男'), (2, '女'))
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
    depart = models.ForeignKey(verbose_name='部门', to="Department",default=1)
    stuff_position_type_choices = ((1, u'工程师助理'),
                                   (2, u'工程师'),
                                   (3, u'主管'),
                                   (4, u'文员'),
                                   (5, u'业务员'),
                                   (6, u'普工'),
                                   (7, u'其他')
                                   )
    stuff_position = models.IntegerField(verbose_name=u'职位',choices=stuff_position_type_choices, default=2, blank=True)
    education_choices = ((1, '博士学位'),
                         (2, '硕士学位'),
                         (3, '本科学位'),
                         (4, '大专'),
                         (5, '高中'),
                         (6, '初中及以下')
                         )
    education = models.IntegerField(verbose_name='学历', choices=education_choices, blank=True, null=True)
    graduation_school = models.CharField(verbose_name='毕业学校', max_length=64, blank=True, null=True)
    major = models.CharField(verbose_name='所学专业', max_length=64, blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='入职日期', blank=True, null=True, auto_now_add=True)

    def __str__(self):  # __str__ on Python 2
        return self.name

    class Meta:
        verbose_name = '员工信息表'
        verbose_name_plural = u"员工信息表"

class Customer(models.Model):
    '''客户信息表'''
    company_name = models.CharField(verbose_name=u"客户公司名称", max_length=64)
    company_type_choices = ((1, u'制造业'),
                             (2, u'轻工业'),
                             (3, u'餐饮业'),
                             (4, u'教育'),
                             (5, u'医疗'),
                             (6, u'航空/航天业'),
                             (7, u'电子信息类'),
                             (8, u'其他')
                             )
    company_type = models.IntegerField(verbose_name=u"公司行业类型", choices=company_type_choices,default=1, blank=True)
    source_type = ((1, u"业务员"),
                   (2, u"介绍人引荐"),
                   (3, u"官方网站"),
                   (4, u"百度广告"),
                   (5, u"其它")
                   )

    source = models.IntegerField(verbose_name=u'客户来源', choices=source_type, default=None, blank=True)  # 统计各渠道的客户量＼成单量,扬长补短
    referral_from = models.TextField(verbose_name="介绍人相关信息", blank=True, null=True, help_text="若此客户是介绍人引荐,请注明信息，日后感谢！")
    consult_business_type_choices = ((1, u'外观件'),
                                     (2, u'内观件'),
                                     (3, u'其他')
                                     )
    consult_business_type = models.IntegerField(verbose_name=u"客户咨询业务项", choices=consult_business_type_choices, blank=True)
    consult_content = models.TextField(verbose_name=u"客户咨询内容详情", help_text=u"客户咨询的大概情况,以及其他备注等...")
    customer_rank_choices = ((1, u'A+级'),  # A+级客户：已下单；
                             (2, u'A级'),  # A级客户：有明显的业务需求，并且预计能够在一个月内下单；
                             (3, u'B级'),  # B级客户：有明显的业务需求，并且预计能够在三个月内下单；
                             (4, u'C级'),  # C级客户：有明显的业务需求，并且预计能够在半年内下单；
                             (5, u'D级'),  # D级客户：有潜在的业务需求的客户或者有明显需求但需要在至少半年后才可能下单；
                             (6, u'E级')  # E级客户：没有需求或者没有任何下单机会，也叫死亡客户。
                             )
    customer_rank = models.IntegerField(verbose_name=u"客户级别", choices=customer_rank_choices,  blank=True)
    secrecy_choices = ((1, u"已签署保密协议"),
                       (2, u"未签署保密协议")
                       )
    secrecy = models.IntegerField(verbose_name=u"保密协议", choices=secrecy_choices,  default=2, blank=True)
    status_choices = ((1, u"未下单"),
                      (2, u"打样阶段"),
                      (3, u"已下单"),
                      (4, u"订单完成"),
                      (5, u"黑名单")
                      )
    status = models.IntegerField(verbose_name=u"客户状态", choices=status_choices,  default=1, help_text=u"选择客户此时的状态", blank=True)
    consultant = models.ForeignKey(to="UserInfo", verbose_name=u"跟进人",limit_choices_to={'depart__title':"市场部"})  # 跟进人只能是市场部的职工
    date = models.DateField(verbose_name=u"咨询日期", auto_now_add=True)
    address = models.CharField(verbose_name=u"客户公司地址", blank=True, null=True,max_length=64)
    negotiator_name = models.CharField(verbose_name=u'联系人姓名', max_length=32)  # max_length 32字节；Django admin、数据库不可以为空


    sex_type = (('male', u'男'), ('female', u'女'))
    sex = models.CharField(verbose_name=u"性别", choices=sex_type, default='male', max_length=32)
    negotiator_position_choices = ((1, u'业务员'),
                                    (2, u'工程师'),
                                    (3, u'主管'),
                                    (4, u'老板'),
                                    (5, u'其他')
                                   )
    negotiator_position = models.IntegerField(verbose_name=u'联系人职位', choices=negotiator_position_choices)
    phone = models.BigIntegerField(verbose_name=u'手机号', unique=True, help_text=u'手机号必须唯一')  # 手机号做为唯一标记客户的值，不能重复

    email = models.EmailField(verbose_name=u'邮箱', blank=True, null=True)
    qq = models.IntegerField(verbose_name=u'QQ号', blank=True, null=True)
    wechat = models.CharField(verbose_name=u'微信', blank=True, null=True,max_length=32)
    msn = models.CharField(verbose_name=u'MSN', blank=True, null=True,max_length=32)
    id_num = models.CharField(verbose_name=u'身份证号', blank=True, null=True, max_length=64)

    def __str__(self):
        return self.company_name

    class Meta:  # 这个是用来在admin页面上展示的，因为默认显示的是表名，加上这个就变成中文啦
        verbose_name = u'客户信息表'
        verbose_name_plural = u"客户信息表"

class CustomerFollowUp(models.Model):
    '''存储客户的后续跟进信息表'''
    customer = models.ForeignKey(Customer,verbose_name=u"客户")
    customer_rank_choices = ((1, u'A+级客户'), #A+级客户：已下单；
                             (2, u'A级客户'), #A级客户：有明显的业务需求，并且预计能够在一个月内下单；
                             (3, u'B级客户'), #B级客户：有明显的业务需求，并且预计能够在三个月内下单；
                             (4, u'C级客户'), #C级客户：有明显的业务需求，并且预计能够在半年内下单；
                             (5, u'D级客户'), #D级客户：有潜在的业务需求的客户或者有明显需求但需要在至少半年后才可能下单；
                             (6, u'E级客户'), #E级客户：没有需求或者没有任何下单机会，也叫死亡客户。
                            )
    customer_rank = models.IntegerField(verbose_name=u"客户级别",choices=customer_rank_choices,default=5)
    secrecy_choices = ((1,u"已签署保密协议"),
                       (2,u"未签署保密协议"),
                      )
    secrecy = models.IntegerField(verbose_name=u"保密协议",choices=secrecy_choices,default=2)
    status_choices = ((1,u"未下单"),
                      (2,u"打样阶段"),
                      (3,u"已下单"),
                      (4,u"订单完成"),
                      (5,u"黑名单"),
                     )
    status = models.IntegerField(verbose_name=u"客户状态",choices=status_choices,default=1,help_text=u"选择客户此时的状态")
    # consultant = models.ForeignKey("UserInfo",verbose_name=u"跟踪人",default=None)
    note = models.TextField(verbose_name=u"跟进内容...",default=None)
    consultant = models.ForeignKey("UserInfo", verbose_name=u"跟进人",limit_choices_to={'depart__title':"市场部"})  # 跟踪顾问只能是市场部的职工
    date = models.DateField(verbose_name=u"跟进日期",auto_now_add=True)

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name = u'客户咨询跟进记录'
        verbose_name_plural = u"客户咨询跟进记录"

class Goods(models.Model):
    '''产品信息表'''
    name = models.CharField(verbose_name='产品名称', max_length=16)
    customer = models.ForeignKey(verbose_name=u"客户",to="Customer")# 一个客户可以有多个产品
    status_choices = ((1, u"打样阶段"),
                      (2, u"量产阶段（未完成）"),
                      (3, u"量产阶段（已完成）")
                     )
    status = models.IntegerField(verbose_name=u"阶段", choices=status_choices, default=1)
    consultant = models.ForeignKey("UserInfo", verbose_name=u"跟进人",limit_choices_to={'depart__title':"市场部"})  # 跟踪顾问只能是市场部的职工

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'产品信息表'
        verbose_name_plural = u"产品信息表"

class Process(models.Model):
    '''部件制程表'''
    name = models.CharField(verbose_name='制程名称', max_length=16)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'部件制程表'
        verbose_name_plural = u"部件制程表"

class Status(models.Model):
    '''部件品质状态表'''
    name = models.CharField(verbose_name='部件品质状态名称', max_length=16)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'部件品质状态表'
        verbose_name_plural = u"部件品质状态表"

class Unqualified(models.Model):
    '''部件品质不良明细表'''
    name = models.CharField(verbose_name='不良类型', max_length=16)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'部件品质不良明细表'
        verbose_name_plural = u"部件品质不良明细表"

class Component(models.Model):
    '''部件信息表'''
    name = models.CharField(verbose_name='部件名称', max_length=16)
    code = models.CharField(verbose_name='部件编号', max_length=16)
    count = models.IntegerField(verbose_name=u'数量')
    unit = models.CharField(verbose_name='单位', max_length=16)
    goods = models.ForeignKey(verbose_name=u"部件所属产品名称",to="Goods")          # 一个产品可以有多个部件
    process = models.ForeignKey(verbose_name=u"部件所属产品制程",to="Process") #一个部件可以有多个制程，一个制程可以有多个部件
    status = models.ForeignKey(verbose_name=u"部件品质状态名称",to="Status")    #一个部件只有一个品质状态

    unqualified_name = models.CharField(verbose_name=u"部件不良类型",blank=True,null=True,max_length=64,help_text=u"良品填（良品）/报废填写(报废)")  #
    position = models.CharField(verbose_name='产品放置区域', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'部件信息表'
        verbose_name_plural = u"部件信息表"

class Bill(models.Model):
    '''产品出/入库单表'''
    name = models.CharField(verbose_name='部件名称', max_length=16)
    code = models.CharField(verbose_name='编号', max_length=16)
    count = models.IntegerField(verbose_name=u'数量')
    unit = models.CharField(verbose_name='单位', max_length=16)
    goods = models.ForeignKey(verbose_name=u"产品名称",to="Goods")    # 一个产品可以有多个部件
    process = models.ForeignKey(verbose_name=u"制程",to="Process")#一个部件可以有多个制程

    status = models.ForeignKey(verbose_name=u"品质状态",to="Status")
    unqualified_name = models.CharField(verbose_name=u"不良类型",blank=True,null=True,max_length=64,help_text=u"良品填（良品）/报废填写(报废)")  #
    stuff_approver = models.ForeignKey(verbose_name='批准者', to="UserInfo",related_name='stuff_approver')
    stuff_executor = models.ForeignKey(verbose_name='执行者', to="UserInfo",related_name='stuff_executor')
    stuff_drawer = models.ForeignKey(verbose_name='制表者', to="UserInfo",related_name='stuff_drawer')
    depart = models.ForeignKey(verbose_name='部门', to="Department")

    bill_type = ((1, u"入库单"),
                 (2, u"出库单")
                )
    bill = models.IntegerField(verbose_name=u"单据类型",choices=bill_type)
    date = models.DateTimeField(verbose_name='日期', auto_now_add=True)

    def __str__(self):
        return self.bill

    class Meta:
        verbose_name = u'产品出/入库单表'
        verbose_name_plural = u"产品出/入库单表"


