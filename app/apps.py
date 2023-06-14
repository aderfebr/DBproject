from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

class RegisterConfig(AppConfig):
    name = 'register'
    verbose_name = "用户管理"     #新添加一行
