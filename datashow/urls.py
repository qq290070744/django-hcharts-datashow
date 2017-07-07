"""datashow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from app01 import views as app01

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^accounts/login/$", app01.acc_login),
    url(r"^accounts/logout/$", app01.acc_logout),
    url(r"^$", app01.index),
    url(r"^pvuv/$", app01.pvuv),
    url(r"^可缩放的时间轴/$", app01.可缩放的时间轴),
    url(r"^百分比堆叠面积图/$", app01.百分比堆叠面积图),
    url(r"^误差线图/$", app01.误差线图),
    url(r"^颜色渐变的饼图/$", app01.颜色渐变的饼图),
    url(r"^带辅助线的气泡图/$", app01.带辅助线的气泡图),
    url(r"^多个图表共用一个提示框/$", app01.多个图表共用一个提示框),
    url(r"^混合图堆叠图/$", app01.混合图堆叠图),
    url(r"^气泡图/$", app01.气泡图),
    url(r"^散点图/$", app01.散点图),
]
