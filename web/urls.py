# -*- encoding: utf-8 -*-

from django.conf.urls import url
from .views import home, EntryCreateView


url_patterns = [
    url(r'^$', home, name='home'),
    url(r'^create/$', EntryCreateView.as_view(), name='create_entry'),
]
