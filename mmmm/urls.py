"""Mmm URL Configuration

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

from mmmm import views

urlpatterns = [
    #url(r'^$/', 'mmmm.views.home', name='home'),
    url(r'^$', views.main, name='main'),
    url(r'^portpholyo/$', views.portpholyo, name='portpholyo'),
    url(r'^CV/$', views.CV, name='CV'),
    url(r'^aboutMe/$', views.aboutMe, name='aboutMe'),
    url(r'^develop/$', views.develop, name='develop'),
    url(r'^hobby/$', views.hobby, name='hobby'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.show_article, name = 'article')
]
