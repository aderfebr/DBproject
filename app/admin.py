from django.apps import AppConfig
from django.contrib import admin
# Register your models here.
from .models import trace_update_staff
admin.site.site_header = '后台管理系统'
admin.site.index_title = '首页'
admin.site.register(trace_update_staff)

