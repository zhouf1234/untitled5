from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

#2019这个默认值，传参不受影响
def blog_list(request,year=2019,month=3):
    print(year)
    print(month)
    return HttpResponse("app02的ok！")