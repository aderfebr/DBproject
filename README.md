# DBproject
```
# 首先将DBproject文件夹下settings.bak更名为settings.py

pip install -r ./requirements.txt
# 安装环境

create database DBproject
#在mysql中新建数据库

python.exe .\manage.py makemigrations
python.exe .\manage.py migrate
#迁移数据库配置

python.exe .\manage.py runserver
# 启动服务
```