# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'pages.views',

    url(r'^pages/$', 'all_pages', name='pages_all_pages'),
    url(r'^pages/(?P<slug>[-\w]+)/$', 'detail', name='pages_detail_page'),
)
