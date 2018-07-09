from django.shortcuts import render,redirect
from wintop import models
from rbac.service import permission


import datetime,os,random,string
from django.core.cache import cache
from static.utils import verify_code
from PMTsmart import settings


def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    err_msg = {}
    # today_str = datetime.date.today().strftime("%Y%m%d")
    # verify_code_img_path = "%s/%s" %(settings.VERIFICATION_CODE_IMGS_DIR,today_str)
    # if not os.path.isdir(verify_code_img_path):os.makedirs(verify_code_img_path,exist_ok=True)
    # random_filename = "".join(random.sample(string.ascii_lowercase,4))
    # random_code = verify_code.gene_code(verify_code_img_path,random_filename)
    # cache.set(random_filename, random_code,300)

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        _verify_code = request.POST.get('verify_code')
        _verify_code_key  = request.POST.get('verify_code_key')


        user = models.UserInfo.objects.filter(name=user, password=pwd).first()
        if user:
            # 只要用户登录成功
            # 设置session_key
            # 权限信息放入session
            # 菜单信息放入session
            current_user = models.UserInfo.objects.filter(name=user).first()
            permission.init_permission(user, request)
            # return redirect('/index/')
            return render(request,'index.html',{'current_user':current_user})
        else:
            err_msg['error'] = "用户名或密码错误!"
            return render(request, 'login.html',{"error_msg":err_msg})
    # else:
    #     err_msg['error'] = "验证码错误!"
    #     return render(request,'login.html',{  "error_msg":err_msg})


def logout(request):
    """
    注销
    :param request:
    :return:
    """
    request.session.clear()
    return redirect('/login/')


def reset_permission(request):
    """
    权限重置
    :param request:
    :return:
    """
    # 找到人
    # 获取这个人的session_key
    # 在session表中将该用户的数据删除。
    # name = "alex"
    # obj = models.UserInfo.objects.filter(name=name).first()
    # permission.reset_permission(obj.session_key,request)
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()
        return render(request,'reset_permission.html',{'user_list':user_list})
    else:
        name = request.POST.get('name')
        obj = models.UserInfo.objects.filter(name=name).first()
        if obj.session_key:
            permission.reset_permission(obj.session_key,request)
        return redirect('/reset/permission/')
def depart(request):
    """
    部门管理
    :param request:
    :return:
    """
    return render(request,'depart.html')

def index(request):
    """
    部门管理
    :param request:
    :return:
    """
    current_user = models.UserInfo.objects.all()
    return render(request,'index.html',{'current_user':current_user})

# def user_detail(request,current_user_id):
#     """
#     用户详情
#     :param request:
#     :return:
#     """
#
#     return render(request,'user_detail.html')

