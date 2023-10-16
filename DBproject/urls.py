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
from django.urls import path
from app import views

urlpatterns = [
    path('',views.home),
    path('api/wuliao/',views.wuliao),
    path('api/kucun/',views.kucun),
    path('api/tiaopei/',views.tiaopei),
    path('api/mps/',views.mps),
    path('api/add_mps/',views.add_mps),
    path('api/clear_mps/',views.clear_mps),
    path('answer/',views.answer)
]
