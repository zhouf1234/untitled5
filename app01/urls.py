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
#from django.contrib import admin
from django.urls import path,re_path
from app01 import views as app01_views


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('blog/2018/10/',views.blog_list),
    #正则表达式的方法分了组:加了（）
    #re_path('blog/(\d{4})/(\d{1,2})/',views.blog_list),
    re_path('blog/(?P<year>\d{4})/(?P<month>\d{1,2})/',app01_views.blog_list),
]
