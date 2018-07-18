"""pj URL Configuration

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
from item import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # ex: http://127.0.0.1:8000/wel
    url(r'^wel$', views.welcome, name='welcome'),
    # ex: http://127.0.0.1:8000/doget/12345
    url(r'^doget/(.*)$', views.doget_execute, name='doget_e'),
#     url(r'^doget/(?P<param1>.*)$', views.doget_execute, name='doget_p'),
    url(r'^item/', include('item.urls')),
    # ex: http://127.0.0.1:8000/showtemp1/
    url(r'^showtemp1/$', views.showtemp1),
    # ex: http://127.0.0.1:8000/showtemp1sc/
    url(r'^showtemp1sc/$', views.showtemp1sc),
    url(r'show/$', views.welcome, name='wel'),

]
