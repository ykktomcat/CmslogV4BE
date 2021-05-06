"""CmslogV4BE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from logs import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cmslogs', views.get_cmslogs),  # 获取所有日志信息的接口
    path('cmslogs/query', views.query_cmslogs),  # 查询日志信息的接口
    path('cmslogs/add', views.add_cmslogs),  # 添加日志的接口
    path('cmslogs/update', views.update_cmslogs),  # 修改日志的接口
    path('cmslog/delete', views.delete_cmslog),  # 单条日志删除的接口
    path('cmslogs/delete', views.delete_cmslogs),  # 批量日志删除的接口
    path('cmslogs/user', views.query_cmsusers),  # 登录用户的接口

    path('cmslogs/getonecmslog', views.update_getone_cmslogs),  #用户修改的接录口
    path('cmslogs/modpwuser', views.modpw_cmsusers),  #用户修改的接录口
    path('cmslogs/export', views.export_comslogs_excel),  #CMS日志导出
    path('cmslogs/info_a', views.info_a),  # 近7天每人新增日志量
    path('cmslogs/info_b', views.info_b),  # 近7天来源系统 日志情况
    path('cmslogs/info_c', views.info_c),  # 近7天日增量
    path('cmslogs/info_d', views.info_d),  # 所有日志公司分布情况
    path('cmslogs/info_e', views.info_e),  #  需求 人为原因 系统原因 占比
]

#放行静态文件
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)