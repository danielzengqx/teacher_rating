"""teacher_system URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^weixin/', views.weixin),    
    url(r'^$',include('home_page.urls')),
    url(r'^register/',include('register.urls')),
    url(r'^login/',include('login.urls')),
    url(r'^rating/',include('rating.urls')),
    url(r'^teacher_info/',include('teacher_info.urls')),
    url(r'^logout/',include('logout.urls')),
    url(r'^video/',include('video.urls')),
    url(r'^comment/',include('comment.urls')),
    url(r'^school_info/',include('school_info.urls')),
    url(r'^teacher_account/', include('teacher_account.urls')),
    url(r'^mx/', views.mx),



]

