"""crowdvisdatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path("test/",views.insert_test_sc),
    path("delete/",views.delete_data),

    path("api/query/",views.staff_query),
    path("api/add_staff/",views.staff_foreignkey),
    path("api/add_staff/insert/",views.add_staff_main),
    path("api/add_staff/update/",views.update_staff_main),
    path("api/add_staff/delete/",views.delete_staff_main),

    path("api/area_query/",views.area_query),            #区域表展示返回位置
    path("api/area_foreignkey/",views.area_foreignkey),  #区域表下拉框位置
    path("api/add_area/",views.add_area_main),           #区域表insert位置
    path("api/update_area/",views.update_area_main),     #区域表update位置
    path("api/delete_area/",views.delete_area_main),     #区域表delete位置

    path("api/device_query/",views.device_query),        #设备表展示返回位置
    path("api/device_foreignkey/",views.device_foreignkey),#设备表下拉框位置
    path("api/add_device/",views.add_device_main),#设备表insert位置
    path("api/update_device/",views.update_device_main),#设备表update位置
    path("api/delete_device/",views.delete_device_main),#设备表delete位置

    path("api/security_view/",views.security_view_query),
    path("api/maintain_view/",views.maintain_view_query),

    path("api/warn/",views.warn_query),
    path("api/deal_warn/",views.deal_warning),
    
    path('api/query/sreport/',views.report_query_s1),              #传staff_id_id
      #传sreport_id_id
    path('api/add/sreport',views.add_sreport),                      #传staff_id_id与sreport_date                
]
