# -*- encoding: utf-8 -*-

from django.conf.urls import url
from .views import (
    EntriesTemplateView, EntryCreateView, InDormitoryTemplateView
)


url_patterns = [
    url(r'^$', EntriesTemplateView.as_view(), name='home'),
    url(r'^indorm', InDormitoryTemplateView.as_view(), name='indorm'),
    url(r'^create/$', EntryCreateView.as_view(), name='create_entry'),
]
