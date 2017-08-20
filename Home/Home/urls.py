"""Home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from Appliance import views
from rest_framework.urlpatterns import format_suffix_patterns
from Appliance.models import Appliance


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home,name="HomePage"),
    url(r'^appliance/(?P<appliance_name>[A-Z][a-z]+)/$', views.ApplianceList.as_view()),
    url(r'^HandleState/(?P<name_of_appliance>[A-Z][a-z]+)/(?P<command>[a-z]+)$',views.StateHandler,name="StateHandler"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
