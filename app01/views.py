from django.shortcuts import render,redirect,HttpResponse
from django.shortcuts import reverse
#reverse：反向解析函数，使传入的参数args不被写死
from django.http import HttpResponse
import datetime
#引入一个http模块中的datetime函数模块；以HTML文档的形式返回当前日期和时间的视图

# Create your views here.
#因为urls的re_path('blog/(\d{4})/(\d{1,2})/',views.blog_list),这句路径传了多个参数，所以这里的要多写个参数
#def blog_list(request,**kwargs):
    #print(kwargs)
    #print(type(kwargs.get('year')))
    #return HttpResponse("OK")


#request:views的一个默认参数，写函数时自动加上
#2019这个默认值，传参不受影响
def blog_list(request,year=2019,month=3,name=None):
    print(year)
    print(month)
    print(name)
    #year = 2016
    #month = 3
    #return redirect(reverse("blog_list",args=(year,month)))
    return HttpResponse("app01的hello......")

def log(request):
    return render(request, "app01/log.html")

def login(request):
    return render(request,"app01/login.html",{"year":2008,"month":10})

#这个views视图会返回一个HttpResponse对象，其中包含生成的响应。
# 每个views视图函数都负责返回一个HttpResponse对象。
def current_datetime(request):
    now = datetime.datetime.now()
    html="<html><body>It is now %s.</body></html>"%now
    return HttpResponse(html)