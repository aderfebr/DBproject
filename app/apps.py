from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'


class BbssConfig(AppConfig):
    name = 'app'
    verbose_name = '用户操作管理系统'

