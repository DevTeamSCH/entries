# -*- encoding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EntriesTemplateView.as_view(), name='home'),
    url(r'^logout/$', views.logout_view,  name='logout'),
    url(r'^indorm$', views.InDormitoryTemplateView.as_view(), name='indorm'),
    url(r'^create/$', views.EntryCreateView.as_view(), name='create_entry'),
]
