

![image](https://github.com/Elegant23435/PMTsmart/raw/master/readmeimgs/1.png)

![image](https://github.com/Elegant23435/PMTsmart/raw/master/readmeimgs/2.png)

1、【项目名称】
PMTsmart

2、【项目描述】
基于RBAC对使用系统的员工进行权限控制。实现不同角色对资源系统数据的增删改查操作。

3、【运行环境+技术点】
Python3/MySQL/wsgi/nginx/Django/CentOS7/BootStrap

4、【实现功能】</br>  
#①五大板块：</br>  
1.欢迎页面：公司简介（公共页面）</br>  
2.员工管理模块：</br>  
			--a.员工基本信息</br>  
			--b.部门基本信息</br>  			
3.产品管理模块：</br>  
			--a.产品基本信息</br>  
			--b.仓库部件信息</br>  
			--c.出/入库单信息</br>  				
4.客户管理模块：</br>  
			--a.客户列表</br>  
			--b.客户根基列表</br>  				
5.重置员工权限模块：</br>  
#②角色管理：</br>  
	--管理员：        员工管理模块（增删改查）、产品管理模块（增删改查）、客户管理模块（增删改查）、重置员工权限模块</br>  
	--老板/总监：     员工管理模块（查）      、产品管理模块（查）      、客户管理模块（查）</br>  
	--市场部员工：    员工管理模块（查）      、产品管理模块（查）      、客户管理模块（增删改查）</br>  
	--生产管理部员工：员工管理模块（查）      、产品管理模块（增删改查）、客户管理模块（无权限）</br>  
	--其余员工角色：  员工管理模块（查）      、产品管理模块（查）      、客户管理模块（无权限） </br>  
#③权限管理：</br>  
	--实现不同的角色拥有不同的权限</br>  
	--细致的权限划分、可以将权限控制到是否允许一按键就可以点击的级别</br>  
	--实现了对用户的权限重置（重置后权限的用户，刷新页面时将强制退出登录页面，重新登录将获取新的权限）</br>  
	--确保权限框架的通用性、使其能轻易迁移到其它项目</br>  
#④后台管理：</br>  
	--开发类似DjangoAdmin一样的通用后台数据管理平台、并可以扩展至其它项目</br>  
	--使用统一的界面模版、不同的角色动态生成业务菜单</br>  
	--实现对数据的增加、修改、删除、模糊搜索、组合搜索</br>  



