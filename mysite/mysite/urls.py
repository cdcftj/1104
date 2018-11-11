"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello,current_datetime

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), #正则表达式，各个配置的名称都是大写的，TEMPLATE_DIRS
    #固定内容，定位符。点号.是除了\n都可以匹配，*前面一个字符匹配零次或多次 ?零次或一次 +一次或多次，
    url(r'^hello/$', hello),
    url(r'^time/$',current_datetime),
]
#时区是UTC'
