from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout(request):
    """注销用户"""
    auth.logout(request)
    return HttpResponseRedirect("/learning_logs/index/")

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        #显示空的注册列表
        form = UserCreationForm()

    else:
        #处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect("/learning_logs/index/")

    return render(request,'register.html',{'form':form})
