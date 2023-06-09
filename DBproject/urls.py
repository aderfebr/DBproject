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
    path("api/query/",views.query),
    path("api/add_staff/",views.add_staff),
    path("api/add_staff/insert/",views.add_staff_main),
    path("api/add_staff/update/",views.update_staff_main),
    path("api/add_staff/delete/",views.delete_staff_main),
]
