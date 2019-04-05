"""untitled5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path,include
from app01 import views
from app01 import urls as app01_urls
from app02 import urls as app02_urls

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('blog/2018/10/',views.blog_list),
    #正则表达式的方法分了组:加了（）；可以用正则表达式写名称
    #re_path('blog/(\d{4})/(\d{1,2})/',views.blog_list),
    re_path('blog/(?P<year>\d{4})/(?P<month>\d{1,2})/',views.blog_list,{'name':'anan'},name='blog_list'),

    #include app的URL confs
    #凡是app01/app02的，都让app01的urls路径的去处理，include的作用
    #path('app01/',include(app01_urls)),
    #path('app02/',include(app02_urls)),

    #namespace:
    #path('app01/',include(app01_urls),namespace='app01'),
    #path('app02/',include(app02_urls),namespace='app02'),

    #适应电脑端所以可以web_login，规则命名反向解析例
    path('login/',views.login,name='login'),
    path('ccccc/',views.log,name='log'),

    path('current_datetime/',views.current_datetime),
]
