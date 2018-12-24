"""home_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.register, name='register'),
    url(r'^signup$',  views.signup, name='signup'),
    url(r'^success',views.success, name='success'),
    url(r'^setting',views.setting, name='setting'),
    url(r'^my_page/(?P<work_id>\d+)$',views.my_page, name='my_page'),
    url(r'^my_page/(?P<work_id>\d+)/edit$',views.edit_page, name='edit_page'),
    url(r'^my_page/change_profile/(?P<work_id>\d+)$',views.change_profile, name='change_profile'),
    url(r'^stu_page/(?P<school_num>\d+)$',views.stu_page, name='stu_page'),


]
