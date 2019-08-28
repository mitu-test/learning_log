from django.conf.urls import url
from django.contrib.auth.views import login
from users import views
urlpatterns = [
    #登录页面
    url(r'^login/$', login,{'template_name':'login.html'}),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),


]